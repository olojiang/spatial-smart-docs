"""
Record the flows in flows.py as MP4 clips (H.264, 1280px wide, no audio).
Usage: SS_USER=... SS_PASSWORD=... python3 tools/capture/record.py [flow-name-prefix]
"""
import asyncio, subprocess, sys, shutil, tempfile
from pathlib import Path
from playwright.async_api import async_playwright
from browser import goto, launch, signed_in_context, APP_URL, STATE, VIEWPORT
from flows import FLOWS

OUT = Path(__file__).resolve().parents[2] / 'docs' / 'public' / 'media' / 'zh'


async def step(page, s):
    kind, *a = s
    if kind == 'click': await page.locator(a[0]).first.click(timeout=8000)
    elif kind == 'fill': await page.locator(a[0]).first.fill(a[1], timeout=8000)
    elif kind == 'type': await page.keyboard.type(a[0], delay=90)
    elif kind == 'press': await page.keyboard.press(a[0])
    elif kind == 'wait': await page.wait_for_timeout(a[0])


async def main(prefix=''):
    OUT.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as pw:
        browser = await launch(pw)
        ctx0, _ = await signed_in_context(pw, browser)  # refresh cached login
        await ctx0.close()
        for name, url, steps in FLOWS:
            if prefix and not name.startswith(prefix):
                continue
            tmp = Path(tempfile.mkdtemp())
            ctx = await browser.new_context(viewport=VIEWPORT, storage_state=str(STATE))
            page = await ctx.new_page()
            await goto(page, APP_URL + url)
            await page.wait_for_timeout(3500)
            # Poor-man's screencast: grab JPEG frames on a timer (works without
            # Playwright's bundled ffmpeg), then encode them with system ffmpeg.
            frames, running = [], True
            async def grab():
                loop = asyncio.get_running_loop()
                while running:
                    frames.append((loop.time(), await page.screenshot(type='jpeg', quality=80)))
            task = asyncio.create_task(grab())
            try:
                for s in steps:
                    await step(page, s)
                print('✓', name)
            except Exception as e:
                print('✗', name, str(e).splitlines()[0])
            running = False
            await task
            await ctx.close()
            # write frames with real timing via concat demuxer
            lst = []
            for i, (t, data) in enumerate(frames):
                f = tmp / f'{i:05d}.jpg'; f.write_bytes(data)
                dur = (frames[i + 1][0] - t) if i + 1 < len(frames) else 0.5
                lst.append(f"file '{f}'\nduration {dur:.3f}")
            (tmp / 'list.txt').write_text('\n'.join(lst) + f"\nfile '{tmp / f'{len(frames)-1:05d}.jpg'}'\n")
            subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(tmp / 'list.txt'),
                            '-vf', 'scale=1280:-2,fps=20', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                            '-crf', '28', '-movflags', '+faststart', '-an', str(OUT / f'{name}.mp4')], check=True)
            shutil.rmtree(tmp)
        await browser.close()

asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else ''))
