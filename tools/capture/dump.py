"""Debug helper: open a URL signed-in and list all data-testids + visible buttons."""
import asyncio, sys, json
from playwright.async_api import async_playwright
from browser import launch, signed_in_context, APP_URL
async def main(path):
    async with async_playwright() as pw:
        b = await launch(pw); ctx, page = await signed_in_context(pw, b)
        from browser import goto; await goto(page, APP_URL + path); await page.wait_for_timeout(5000)
        await page.screenshot(path='/tmp/dump.png')
        data = await page.evaluate('''() => [...document.querySelectorAll('[data-testid],button,[role=tab]')].filter(e=>true).map(e=>[e.getAttribute('data-testid')||'', (e.innerText||e.title||e.getAttribute('aria-label')||'').trim().slice(0,30)])''')
        for d in data: print(d)
        await b.close()
asyncio.run(main(sys.argv[1] if len(sys.argv)>1 else ''))
