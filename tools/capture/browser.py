"""
Shared Playwright helpers for the capture tools.

- Logs into Pinefield SSO, solving the 6-digit image captcha with ddddocr.
  The captcha expires within seconds, so we always: click 换一个 -> read -> type -> submit
  immediately, retrying with a fresh captcha on failure.
- Credentials come from env vars SS_USER / SS_PASSWORD (never commit them).
- The signed-in session is cached in .auth/state.json (git-ignored).
"""
from __future__ import annotations
import asyncio, base64, os, urllib.parse, urllib.request
from pathlib import Path
from playwright.async_api import async_playwright, Browser, BrowserContext, Page

APP_URL = 'https://alpha.pinefield.cn/pinefield.spatial-smart/'
SSO_URL = ('https://alpha.pinefield.cn/pinefield.sso/#/login?url='
           + urllib.parse.quote(APP_URL, safe='') + '&apps=spacetop')
STATE = Path(__file__).parent / '.auth' / 'state.json'
VIEWPORT = {'width': 1440, 'height': 900}


def _proxy() -> dict | None:
    """Honour HTTPS_PROXY (with credentials) if the environment sets one."""
    raw = urllib.request.getproxies().get('https')
    if not raw:
        return None
    u = urllib.parse.urlparse(raw)
    p = {'server': f'{u.scheme}://{u.hostname}:{u.port}'}
    if u.username:
        p['username'] = urllib.parse.unquote(u.username)
        p['password'] = urllib.parse.unquote(u.password or '')
    return p


async def goto(page: Page, url: str, tries: int = 4) -> None:
    """page.goto with retries: the network path to the site is occasionally flaky."""
    for i in range(tries):
        try:
            await page.goto(url, wait_until='load', timeout=60000)
            return
        except Exception:
            if i == tries - 1:
                raise
            await asyncio.sleep(5 * (i + 1))


async def launch(pw) -> Browser:
    exe = os.environ.get('CHROMIUM_PATH') or ('/usr/bin/chromium' if Path('/usr/bin/chromium').exists() else None)
    return await pw.chromium.launch(executable_path=exe, args=['--no-sandbox'], proxy=_proxy())


async def _read_captcha(page: Page, ocr) -> str:
    img = page.locator('img[src^="data:image"]').first
    data = base64.b64decode((await img.get_attribute('src')).split(',', 1)[1])
    text = ocr.classification(data)
    return ''.join(ch for ch in text if ch.isdigit())


async def login(ctx: BrowserContext, attempts: int = 12) -> Page:
    import ddddocr  # lazy import: heavy
    ocr = ddddocr.DdddOcr(show_ad=False)
    user, pwd = os.environ['SS_USER'], os.environ['SS_PASSWORD']
    page = await ctx.new_page()
    await goto(page, SSO_URL); await page.wait_for_timeout(2000)
    for i in range(attempts):
        await page.fill('#form_item_username', user)
        await page.fill('#form_item_passwd', pwd)
        await page.get_by_text('换一个').click()
        await page.wait_for_timeout(300)
        code = await _read_captcha(page, ocr)
        if len(code) != 6:
            continue
        await page.fill('#form_item_digits', code)
        await page.locator('button[type=submit], button:has-text("登")').first.click()
        try:
            await page.wait_for_url('**/pinefield.spatial-smart/**', timeout=6000)
            print(f'login ok after {i + 1} attempt(s)')
            STATE.parent.mkdir(exist_ok=True)
            await ctx.storage_state(path=str(STATE))
            return page
        except Exception:
            pass
    raise RuntimeError('login failed: captcha not solved')


async def signed_in_context(pw, browser: Browser) -> tuple[BrowserContext, Page]:
    """Reuse cached session when still valid, otherwise log in again."""
    if STATE.exists():
        ctx = await browser.new_context(viewport=VIEWPORT, storage_state=str(STATE), device_scale_factor=2)
        page = await ctx.new_page()
        await goto(page, APP_URL)
        await page.wait_for_timeout(1500)
        if 'pinefield.sso' not in page.url:
            return ctx, page
        await ctx.close()
    ctx = await browser.new_context(viewport=VIEWPORT, device_scale_factor=2)
    page = await login(ctx)
    return ctx, page


if __name__ == '__main__':
    async def _main():
        async with async_playwright() as pw:
            b = await launch(pw)
            ctx, page = await signed_in_context(pw, b)
            await page.wait_for_timeout(2500)
            await page.screenshot(path='/tmp/after_login.png')
            print(page.url)
            await b.close()
    asyncio.run(_main())
