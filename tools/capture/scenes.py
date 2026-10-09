"""
Declarative list of screenshots used in the manual.

Each scene: (name, url_suffix, steps). Steps are tuples:
  ('click', selector) | ('hover', selector) | ('fill', selector, text) | ('press', key)
  ('wait', ms) | ('shot',)  -> saves docs/public/media/<lang>/<name>.png
Selectors are Playwright selectors; prefer data-testid / visible text.
If the site changes, fix the selector here and re-run `npm run capture`.
"""
SPACE = 'encId=37143acf-9c9a-47a2-a435-130ee2da5aa2&spaceName=%5B%E5%8B%BF%E5%88%A0%5D%E6%B5%8B%E8%AF%95SituosV2.0.1'
T = lambda tid: f'[data-testid="{tid}"]'

SCENES = [
    # ---------- shell ----------
    ('shell-no-space', '', [('wait', 1500), ('shot',)]),
    ('shell-space-picker', '', [('click', T('web-workspace-scene-select')), ('wait', 800), ('shot',)]),
    ('shell-search', f'?{SPACE}', [('click', T('web-workspace-global-search')), ('wait', 600),
                                     ('fill', 'input[placeholder*="搜索所有会话"]', '客流'), ('wait', 400), ('shot',)]),
    ('shell-user-menu', f'?module=service&{SPACE}', [('click', T('sidebar-user-menu-trigger')), ('wait', 500), ('shot',)]),
    ('shell-settings-general', f'?{SPACE}', [('click', T('sidebar-user-menu-trigger')), ('click', 'text=设置'), ('wait', 3000), ('shot',)]),
    ('shell-settings-skills', None, [('click', 'role=tab[name="Skills"] >> nth=0'), ('wait', 600), ('shot',)]),
    ('shell-settings-proxy', None, [('click', 'role=tab[name="Proxy"]'), ('wait', 400), ('shot',)]),
    ('shell-settings-cli', None, [('click', 'role=tab[name="Claude CLI"]'), ('wait', 400), ('shot',), ('press', 'Escape')]),
    ('shell-collapsed', f'?module=service&{SPACE}', [('click', 'button[title="折叠应用导航"], [aria-label="折叠应用导航"]'), ('wait', 600), ('shot',)]),
    ('shell-dark', f'?module=service&{SPACE}', [('click', 'role=button[name="切换主题"]'), ('wait', 600), ('shot',),
                                                ('click', 'role=button[name="切换主题"]')]),
    ('shell-english', f'?module=service&{SPACE}', [('click', 'role=button[name="切换到 English"]'), ('wait', 800), ('shot',),
                                                   ('click', 'role=button[name="Switch to 中文"]'), ('wait', 500)]),
    # 'SSO' = fresh signed-out browser on the login page
    ('login-sso', 'SSO', [('wait', 1500), ('shot',)]),
    # ---------- 应用 ----------
    ('app-home', f'?module=app&{SPACE}', [('wait', 800), ('shot',)]),
    ('app-workspace-menu', f'?module=app&{SPACE}', [('click', 'button:has-text("工作空间")'), ('wait', 500), ('shot',)]),
    ('app-model-picker', f'?module=app&{SPACE}', [('click', 'button:has-text("Kimi K2.6")'), ('wait', 500), ('shot',)]),
    ('app-conversation', '', [('wait', 3000), ('click', T('navigation') + ' >> text=你能帮我做什么 >> nth=0'), ('wait', 5000), ('shot',)]),
    ('app-pin-menu', None, [('click', T('workbench') + ' >> role=button[name="固定标签页"]'), ('wait', 500), ('shot',), ('press', 'Escape')]),
    ('app-preview-tab', None, [('click', T('workbench') + ' >> text=预览 >> nth=0'), ('wait', 3000), ('shot',)]),
    ('app-space-tab', None, [('click', T('workbench') + ' >> text=空间 >> nth=0'), ('wait', 3000), ('shot',)]),
    # ---------- 智能体 ----------
    ('agent-no-space', '?module=agent', [('wait', 800), ('shot',)]),
    ('agent-list', f'?module=agent&{SPACE}', [('wait', 1200), ('shot',)]),
    ('agent-config', f'?module=agent&{SPACE}', [('click', 'text=文档示例智能体 >> nth=0'), ('wait', 1500), ('shot',)]),
    ('agent-yaml', None, [('click', 'text=YAML >> nth=0'), ('wait', 600), ('shot',)]),
    ('agent-pin-menu', None, [('click', T('web-workspace-agent-tab-add')), ('wait', 400), ('shot',), ('press', 'Escape')]),
    ('agent-row-menu', f'?module=agent&{SPACE}', [('hover', '[data-testid^="seele-agent-row-"] >> nth=0'), ('click', '[data-testid^="seele-agent-actions-"] >> nth=0'), ('wait', 400), ('shot',), ('press', 'Escape')]),
    ('agent-new-general', f'?module=agent&{SPACE}', [('click', T('web-workspace-agent-new-agent')), ('wait', 600), ('shot',)]),
    ('agent-new-scheduled', None, [('click', 'role=dialog >> text=定时'), ('wait', 400), ('shot',)]),
    ('agent-new-event', None, [('click', 'role=dialog >> text=事件触发'), ('wait', 400), ('shot',), ('press', 'Escape')]),
    # ---------- 服务 ----------
    ('service-empty', f'?module=service&{SPACE}', [('wait', 800), ('shot',)]),
    ('service-overview', f'?module=service&{SPACE}', [('click', T('service-module-row-svc-booth-flow')), ('wait', 1500), ('shot',)]),
    ('service-code', None, [('click', T('web-workspace-service-tab-code')), ('wait', 1200), ('shot',)]),
    ('service-versions', None, [('click', T('web-workspace-service-tab-versions')), ('wait', 600), ('shot',)]),
    ('service-logs', None, [('click', T('web-workspace-service-tab-logs')), ('wait', 600), ('shot',)]),
    ('service-logs-failed', None, [('click', T('web-workspace-service-workbench') + ' >> text=失败 >> nth=0'), ('wait', 400), ('shot',)]),
    ('service-conversation-2', None, [('click', T('service-module-session-svc-booth-flow-session-2')), ('wait', 1200), ('shot',)]),
    ('service-row-menu', f'?module=service&{SPACE}', [('hover', T('service-module-row-svc-booth-flow')),
                                                      ('click', 'role=button[name="项目菜单"] >> nth=0'), ('wait', 400), ('shot',), ('press', 'Escape')]),
    ('service-new', f'?module=service&{SPACE}', [('click', T('service-module-create')), ('wait', 600),
                                                 ('fill', 'textarea[placeholder*="起始时间"]', '根据传入的起始时间和结束时间，返回人流折线图数据'), ('wait', 300), ('shot',), ('press', 'Escape')]),
]
