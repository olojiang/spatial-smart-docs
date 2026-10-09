# Preferences

Click **Avatar → Settings** (头像 → 设置) in the bottom-left corner to open the **Settings** dialog (subtitle: "Configure Claude Code preferences" (配置 Claude Code 偏好设置)). It has 4 tabs. **Save settings** (保存设置) in the top-right corner becomes clickable only after you change something.

::: info What do these settings affect?
Spatial Smart's AI coding is built on Claude Code. These settings control the AI's default behavior in **new conversations** — prompts, permissions, log level, and so on.
:::

## General

<Shot src="/media/zh/shell-settings-general.png" caption="General settings" />

| Setting | Default | Description |
| --- | --- | --- |
| Theme (主题) | Light | Dark / Gray / Light / Custom |
| Include "Co-authored by Claude" (包含 "Co-authored by Claude") | On | Adds a Claude co-author credit to commits |
| Verbose output (Verbose 输出) | Off | Shows full Bash and command output |
| Chat history retention days (聊天记录保留天数) | 30 | Chat history older than this is cleaned up |
| Enable Analytics (启用 Analytics) | On | Collects anonymous usage patterns only — no personal data or code; turn off anytime |
| Remember open tabs (记住打开的标签页) | On | Restores your last tabs when you reopen |
| Show welcome guide on startup (启动时显示欢迎引导) | On | The onboarding guide on first visit |
| Read-only share preview on by default (只读分享页预览默认开启) | On | Expands the preview by default when others open your read-only share page |
| Show Open API (显示 Open API) | Off | When on, an Open API settings section appears |
| Select Variant (选择 Variant) | digital-native | Options: `digital-native` / `attention` |
| Frontend debug mode (前端调试模式) | Off | Toggles `localStorage.debug`; use it when troubleshooting frontend issues |
| Export logs (导出日志) | — | **View logs** (查看日志) and **Export logs** (导出日志); attach logs when reporting issues |

## Skills

<Shot src="/media/zh/shell-settings-skills.png" caption="Skills: Installed / Marketplace" />

Manage workspace and global skills (enable / disable), and invoke them in conversations with `/skill-name`.

- **Installed / Marketplace** (已安装 / 市场): switch between your installed skills and the marketplace.
- **Refresh** (刷新) reloads the list; **Filter** (筛选) searches by name.
- With no workspace selected, you'll see: "No workspace selected; workspace skills can't be shown." (未选择工作空间，暂无法展示工作空间 skills。)

## Proxy

<Shot src="/media/zh/shell-settings-proxy.png" caption="Proxy: configure a proxy for Claude API requests" />

| Field | Example |
| --- | --- |
| Enable Proxy | The fields below become editable only when this is on |
| HTTP Proxy | `http://proxy.example.com:28323` |
| HTTPS Proxy | `http://proxy.example.com:28323` |
| No Proxy | `localhost,127.0.0.1,.example.com` (comma-separated addresses that bypass the proxy) |
| All Proxy (optional) | `socks5://proxy.example.com:1080` |

## Claude CLI

<Shot src="/media/zh/shell-settings-cli.png" caption="Claude CLI: runtime options, prompts, and permission rules" />

**Runtime and debugging**

| Setting | Flag | Default |
| --- | --- | --- |
| Verbose logging (详细日志) | `--verbose` | On |
| Debug mode (调试模式) | `--debug` | Off |
| Debug log file (调试日志文件) | `--debug-file` | Empty |

**Prompts and behavior**

| Setting | Flag | Purpose |
| --- | --- | --- |
| System prompt (系统提示词) | `--system-prompt` | Sets the default system prompt for new conversations |
| Append system prompt (追加系统提示词) | `--append-system-prompt` | Appends instructions after the default prompt, e.g. team coding conventions |
| Disable Slash Commands (禁用 Slash Commands) | `--disable-slash-commands` | Disables all slash commands / skills in new conversations |

**Permission rules** (权限规则): control which tools Claude Code can use, and with what arguments.

- **Allow Rules**: tools that can be used without asking; if none are configured, the AI asks for permission before using a tool.
- **Deny Rules**: tools that are blocked.

| Rule example | Meaning |
| --- | --- |
| `Bash` | Allow all Bash commands |
| `Bash(npm run build)` | Allow only this command |
| `Bash(npm run test:*)` | Allow commands starting with `npm run test:` |
| `Read(~/.zshrc)` | Allow reading the specified file |
| `Edit(docs/**)` | Allow editing files under the docs directory |

At the very bottom, **Raw Settings (JSON)** shows the raw configuration saved to `~/.spatial-smart-cc/settings.json`.
