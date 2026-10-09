"""
Crawl the live app and record, per module/view, every visible data-testid, button,
tab and form field into snapshot/sitemap.new.json. Compare with the committed
snapshot via `npm run diff:snapshot`, then promote the new file once docs are updated.

Each page lists the doc pages that describe it (`docs`) so the diff tells you
exactly which chapters to revisit.
"""
import asyncio, json, datetime
from pathlib import Path
from playwright.async_api import async_playwright
from browser import goto, launch, signed_in_context, APP_URL
from scenes import SPACE

ROOT = Path(__file__).resolve().parents[2]
PAGES = [
    # id, menu path, url suffix, docs that describe it, optional click before crawl
    ('shell', ['界面'], '', ['guide/interface', 'guide/space'], None),
    ('app', ['应用'], f'?module=app&{SPACE}', ['apps/chat', 'apps/workbench'], None),
    ('agent', ['智能体'], f'?module=agent&{SPACE}', ['agents/overview', 'agents/manage'], None),
    ('agent-new', ['智能体', '新建智能体'], f'?module=agent&{SPACE}', ['agents/create'], '[data-testid="web-workspace-agent-new-agent"]'),
    ('service', ['服务'], f'?module=service&{SPACE}', ['services/overview'], None),
    ('service-detail', ['服务', '服务工作区'], f'?module=service&{SPACE}', ['services/workbench'], '[data-testid="service-module-row-svc-booth-flow"]'),
    ('service-new', ['服务', '新建服务'], f'?module=service&{SPACE}', ['services/create'], '[data-testid="service-module-create"]'),
    ('settings', ['设置'], f'?{SPACE}', ['settings/preferences'], '[data-testid="sidebar-user-menu-trigger"] >> nth=0'),
]

JS = '''() => {
  const vis = (e) => !!(e.offsetWidth || e.offsetHeight || e.getClientRects().length);
  const txt = (e) => (e.getAttribute('aria-label') || e.title || e.innerText || e.placeholder || '').trim().split('\\n')[0].slice(0, 40);
  const uniq = (a) => [...new Set(a.filter(Boolean))].sort();
  return {
    actions: uniq([...document.querySelectorAll('button,[role=button],[role=menuitem]')].filter(vis).map(txt)),
    tabs: uniq([...document.querySelectorAll('[role=tab]')].filter(vis).map(txt)),
    fields: uniq([...document.querySelectorAll('input,textarea,select,[role=combobox]')].filter(vis).map(e => e.placeholder || e.getAttribute('aria-label') || e.name || e.type)),
    testids: uniq([...document.querySelectorAll('[data-testid]')].filter(vis).map(e => e.dataset.testid)),
  };
}'''


async def main():
    out = {'capturedAt': datetime.datetime.now().isoformat(timespec='seconds'), 'pages': []}
    async with async_playwright() as pw:
        b = await launch(pw)
        ctx, page = await signed_in_context(pw, b)
        for pid, menu, url, docs, pre in PAGES:
            await goto(page, APP_URL + url)
            await page.wait_for_timeout(4000)
            if pre:
                await page.locator(pre).first.click()
                await page.wait_for_timeout(1500)
                if pid == 'settings':
                    await page.get_by_text('设置', exact=True).first.click(); await page.wait_for_timeout(2500)
            data = await page.evaluate(JS)
            out['pages'].append({'id': pid, 'menuPath': menu, 'url': url.split('&encId')[0] or '/', 'docs': docs, **data})
            print('✓', pid, len(data['actions']), 'actions')
        await b.close()
    dest = ROOT / 'snapshot' / 'sitemap.new.json'
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print('wrote', dest)

asyncio.run(main())
