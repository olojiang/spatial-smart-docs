# 偏好设置

点击左下角 **头像 → 设置**，打开「设置」弹窗（副标题：配置 Claude Code 偏好设置）。共有 4 个标签页。修改任意一项后，右上角的 **保存设置** 才会变为可点击。

::: info 这些设置影响什么？
Spatial Smart 的 AI 编码能力基于 Claude Code。这里的设置决定 AI 在**新会话**中的默认行为，例如提示词、权限和日志级别。
:::

## General（通用）

<Shot src="/media/zh/shell-settings-general.png" caption="General：通用设置" />

| 设置项 | 默认 | 说明 |
| --- | --- | --- |
| 主题 | 浅色 | 深色 / 灰色 / 浅色 / 自定义 |
| 包含 "Co-authored by Claude" | 开 | 提交代码时附带 Claude 协作者署名 |
| Verbose 输出 | 关 | 显示完整的 Bash 和命令输出 |
| 聊天记录保留天数 | 30 | 超过天数的聊天记录将被清理 |
| 启用 Analytics | 开 | 仅收集匿名使用模式，不收集个人数据或代码，可随时关闭 |
| 记住打开的标签页 | 开 | 重新打开时恢复上次的标签页 |
| 启动时显示欢迎引导 | 开 | 首次进入时的新手引导 |
| 只读分享页预览默认开启 | 开 | 别人打开你的只读分享页时默认展开预览 |
| 显示 Open API | 关 | 打开后出现 Open API 设置区域 |
| 选择 Variant | digital-native | 可选 `digital-native` / `attention` |
| 前端调试模式 | 关 | 切换 `localStorage.debug`，排查前端问题时使用 |
| 导出日志 | — | 「查看日志」「导出日志」，反馈问题时附上日志 |

## Skills

<Shot src="/media/zh/shell-settings-skills.png" caption="Skills：已安装 / 市场" />

管理工作空间与全局 skills（启用 / 禁用），并通过 `/skill-name` 在对话中调用。

- **已安装 / 市场**：切换查看已安装的技能或去市场挑选。
- **刷新**：重新加载列表；**筛选**：按名称搜索。
- 未选择工作空间时提示：「未选择工作空间，暂无法展示工作空间 skills。」

## Proxy（代理）

<Shot src="/media/zh/shell-settings-proxy.png" caption="Proxy：为 Claude API 请求配置代理" />

| 字段 | 示例 |
| --- | --- |
| Enable Proxy | 开启后下列输入框才可编辑 |
| HTTP Proxy | `http://proxy.example.com:28323` |
| HTTPS Proxy | `http://proxy.example.com:28323` |
| No Proxy | `localhost,127.0.0.1,.example.com`（逗号分隔，不走代理的地址） |
| All Proxy（选填） | `socks5://proxy.example.com:1080` |

## Claude CLI

<Shot src="/media/zh/shell-settings-cli.png" caption="Claude CLI：运行参数、提示词与权限规则" />

**运行与调试**

| 设置 | 对应参数 | 默认 |
| --- | --- | --- |
| 详细日志 | `--verbose` | 开 |
| 调试模式 | `--debug` | 关 |
| 调试日志文件 | `--debug-file` | 空 |

**提示词与行为**

| 设置 | 对应参数 | 用途 |
| --- | --- | --- |
| 系统提示词 | `--system-prompt` | 为新会话设置默认系统提示词 |
| 追加系统提示词 | `--append-system-prompt` | 在默认提示词后追加说明，例如团队编码规范 |
| 禁用 Slash Commands | `--disable-slash-commands` | 新会话中禁用所有 Slash 命令 / skills |

**权限规则**：控制 Claude Code 可以使用哪些工具及其参数。

- **Allow Rules**：允许直接使用的工具；未配置时，AI 使用工具前会征求许可。
- **Deny Rules**：禁止使用的工具。

| 规则示例 | 含义 |
| --- | --- |
| `Bash` | 允许所有 Bash 命令 |
| `Bash(npm run build)` | 只允许这一条命令 |
| `Bash(npm run test:*)` | 允许以 `npm run test:` 开头的命令 |
| `Read(~/.zshrc)` | 允许读取指定文件 |
| `Edit(docs/**)` | 允许编辑 docs 目录下的文件 |

最底部的 **Raw Settings (JSON)** 显示保存到 `~/.spatial-smart-cc/settings.json` 的原始配置。
