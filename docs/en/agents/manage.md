# Configure and test-run

Click an agent in the list on the left. Its **configuration** appears in the middle, and the **Agent preview** (智能体预览) chat appears on the right.

## Top actions

| Button | What it does |
| --- | --- |
| **Stop** (停止) / **Start** (启动) | Stops a running agent (you can start it again afterward) |
| **Save** (保存) | Becomes clickable after you change the configuration; saves your changes |
| **Config / YAML** (配置 / YAML) | Switches between the form view and the YAML text view |

## Config view

<Shot src="/media/zh/agent-config.png" caption="Config view" />

| Field | Description |
| --- | --- |
| Name (名称) | Edit it here to **rename** the agent |
| Model (模型) | Defaults to "PF-H1-Auto (default)" (PF-H1-Auto（默认）), with "Currently active: PF-H1-Auto" (当前生效：PF-H1-Auto) shown below |
| Background knowledge (背景知识) | Business, space, and domain context the agent needs |
| Responsibilities (职责) | What the agent should do, e.g. "Provide accurate, actionable advice based on the current space and project context." |
| Run mode (运行方式) | Read-only; shows the type, which can only be chosen at creation |
| Space ID / Agent ID (空间 ID / 智能体 ID) | Read-only; share these with your administrator when troubleshooting |

## YAML view

Useful for bulk edits or copying a configuration. The description reads: "You can save the name, role, background knowledge, responsibilities, and model. Edit triggers on the Config page; Agent ID and Space ID can't be changed via YAML." (可保存名称、角色、背景知识、职责和模型。触发器请在「配置」页编辑；Agent ID、空间 ID 不可通过 YAML 修改。)

<Shot src="/media/zh/agent-yaml.png" caption="YAML view" />

```yaml
agent:
  agent_id: "1de85ef1-…"          # 只读 (read-only)
  enclosure_id: "37143acf-…"      # 空间 ID，只读 (space ID, read-only)
  name: "文档示例智能体"
  role: "根据当前空间与项目上下文，为用户提供准确、可执行的建议。"
  background_knowledge: ""
  responsibilities: "…"
  model_name: "PF-H1-Auto"
```

## Chat with the agent (test-run)

The **Agent preview** (智能体预览) on the right shows "Continuous chat with *agent name* · Running" (与 *智能体名* 连续对话 · 运行中).

::: steps
1. Type a question in the input box at the bottom (<kbd>Enter</kbd> to send, <kbd>Shift</kbd> + <kbd>Enter</kbd> for a new line).
2. The platform starts a **real test run** through Seele; the preview keeps the context of this session.
3. Use **History** (历史会话) to view past conversations, and **New session** (新建会话) to start a fresh context (grayed out when there are no sessions yet, with the hint "No sessions yet" (当前还没有会话)).
:::

## MCPs, Skills, and the Skill store

Click **＋** (**Pin tab** (固定标签页)) in the top-right corner of the workbench to add three tabs:

<Shot src="/media/zh/agent-pin-menu.png" caption="Pin tab: MCPs / Skills / Skill store" />

| Tab | What it does |
| --- | --- |
| **MCPs** | View and manage the MCP tools available to the agent (external capabilities) |
| **Skills** | View the skills enabled for the agent |
| **Skill store** (Skill 商店) | Browse and add new skills |

Tabs you've added disappear from the menu; once all three are added, the menu is empty.

## The Actions menu in the list

Hover over an agent in the list, and a round **Actions** (操作) button appears on the right:

<Shot src="/media/zh/agent-row-menu.png" caption="Actions menu: Edit config / Stop / Delete Agent" />

| Menu item | What it does |
| --- | --- |
| Edit config (编辑配置) | Opens the configuration editor |
| Stop (停止) | Stops the agent |
| Delete Agent (删除 Agent) | ⚠️ Permanently deletes it — this can't be undone |

::: danger Confirm before deleting
Deleted agents can't be recovered. Don't casually delete agents in shared spaces (names containing "[勿删]", "do not delete").
:::
