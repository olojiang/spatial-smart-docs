#!/usr/bin/env bash
# One-time setup for the capture tools (screenshots, clips, snapshot crawl).
# Uses system Chromium when Playwright's bundled browser is unavailable (e.g. linux-arm64).
set -e
cd "$(dirname "$0")"
python3 -m pip install -q -r requirements.txt
python3 -m playwright install chromium 2>/dev/null || {
  echo "Playwright browser download failed; installing system chromium"
  (sudo apt-get install -y -q chromium || brew install --cask chromium) >/dev/null
}
command -v ffmpeg >/dev/null || echo "⚠ install ffmpeg to record clips (record.py)"
echo "✓ capture tools ready"
