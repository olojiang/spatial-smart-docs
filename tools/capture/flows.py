"""
Short screen recordings (muted, looped in the docs via <Demo>).
Same step grammar as scenes.py, minus ('shot',). Output: docs/public/media/zh/<name>.mp4
"""
from scenes import SPACE, T

FLOWS = [
    ('flow-switch-space-and-modules', '', [
        ('wait', 1200), ('click', T('web-workspace-scene-select')), ('wait', 900),
        ('click', 'text=[勿删]测试SituosV2.0.1 >> nth=0'), ('wait', 1500),
        ('click', T('web-workspace-module-agent')), ('wait', 1500),
        ('click', T('web-workspace-module-service')), ('wait', 1500),
        ('click', T('web-workspace-module-app')), ('wait', 1200)]),
    ('flow-new-agent-types', f'?module=agent&{SPACE}', [
        ('wait', 1000), ('click', T('web-workspace-agent-new-agent')), ('wait', 1200),
        ('fill', 'input[placeholder*="名字"]', '客流日报助手'), ('wait', 800),
        ('click', 'role=dialog >> text=定时'), ('wait', 1400),
        ('click', 'role=dialog >> [role=combobox] >> nth=0'), ('wait', 1400), ('press', 'Escape'),
        ('click', 'role=dialog >> text=事件触发'), ('wait', 1800), ('press', 'Escape'), ('wait', 600)]),
    ('flow-service-workbench', f'?module=service&{SPACE}', [
        ('wait', 1000), ('click', T('service-module-row-svc-booth-flow')), ('wait', 2000),
        ('click', T('web-workspace-service-tab-code')), ('wait', 1800),
        ('click', T('web-workspace-service-tab-versions')), ('wait', 1600),
        ('click', T('web-workspace-service-tab-logs')), ('wait', 1400),
        ('click', T('web-workspace-service-workbench') + ' >> text=失败 >> nth=0'), ('wait', 1400),
        ('click', T('web-workspace-service-tab-overview')), ('wait', 1200)]),
    ('flow-app-chat', f'?module=app&{SPACE}', [
        ('wait', 1000), ('click', '.ProseMirror'), ('type', '用一句话介绍一下你自己'), ('wait', 600),
        ('press', 'Enter'), ('wait', 22000)]),
]
