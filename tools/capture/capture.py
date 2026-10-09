"""
Re-shoot every screenshot in scenes.py.
Usage: SS_USER=... SS_PASSWORD=... python3 tools/capture/capture.py [scene-name-prefix]
Writes docs/public/media/zh/<scene>.png (2x, 1440x900 viewport).
"""
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright
from browser import goto, launch, signed_in_context, APP_URL, SSO_URL, VIEWPORT
from scenes import SCENES

OUT = Path(__file__).resolve().parents[2] / 'docs' / 'public' / 'media' / 'zh'


async def run_step(page, step, name):
    kind, *args = step
    if kind == 'click':
        await page.locator(args[0]).first.click(timeout=8000)
    elif kind == 'hover':
        await page.locator(args[0]).first.hover(timeout=8000)
    elif kind == 'fill':
        await page.locator(args[0]).first.fill(args[1], timeout=8000)
    elif kind == 'press':
        await page.keyboard.press(args[0])
    elif kind == 'wait':
        await page.wait_for_timeout(args[0])
    elif kind == 'shot':
        await page.screenshot(path=str(OUT / f'{name}.png'))


async def main(prefix=''):
    OUT.mkdir(parents=True, exist_ok=True)
    ok, failed = 0, []
    async with async_playwright() as pw:
        browser = await launch(pw)
        ctx, page = await signed_in_context(pw, browser)
        for name, url, steps in SCENES:
            if prefix and not name.startswith(prefix):
                continue
            try:
                if url == 'SSO':  # signed-out page in a throwaway context
                    anon = await browser.new_context(viewport=VIEWPORT, device_scale_factor=2)
                    p2 = await anon.new_page(); await goto(p2, SSO_URL)
                    for step in steps:
                        await run_step(p2, step, name)
                    await anon.close(); ok += 1; print('✓', name); continue
                if url is not None:  # None = continue from previous scene's state
                    await goto(page, APP_URL + url)
                    await page.wait_for_timeout(3500)
                for step in steps:
                    await run_step(page, step, name)
                ok += 1
                print('✓', name)
            except Exception as e:
                failed.append(name)
                print('✗', name, str(e).splitlines()[0])
        await browser.close()
    print(f'{ok} ok, {len(failed)} failed: {failed}')

asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else ''))
