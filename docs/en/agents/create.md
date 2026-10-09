# Create an agent

<Demo src="/media/zh/flow-new-agent-types.mp4" caption="Create an agent: switch between General, Scheduled, and Event-triggered" />

::: steps
1. [Select a space](/en/guide/space) at the top (the button is grayed out until you do).
2. Switch to the **Agents** (智能体) module and click **New agent** (新建智能体) on the left.
3. Choose a type at the top of the dialog: **General / Scheduled / Event-triggered** (通用 / 定时 / 事件触发).
4. Fill in the fields as described below.
5. Click **Create agent** (创建智能体). The button briefly shows "Creating…" (创建中…), then the dialog closes, "Agent created." (智能体已创建。) appears in the top-right corner, and the new agent opens.
:::

The description under the dialog title reads: "Choose a type and fill in the configuration. The agent joins the current space once created." (选择类型并填写配置，创建后加入当前空间。)

## 💬 General

> A general-purpose agent you can chat with anytime. Once created, it lives in your space; talk to it whenever you like, and it works according to the responsibilities you set.

<Shot src="/media/zh/agent-new-general.png" caption="General type" />

| Field | Required | Description / example |
| --- | --- | --- |
| Agent name (智能体名称) | ✅ | Give the agent a name, e.g. "Foot-traffic advisor" |
| Background knowledge (背景知识) | Optional | Business context or domain knowledge the agent should know |
| Responsibilities (职责) | Optional | e.g. Analyze data trends and generate a daily summary. If left blank, a default is generated |

The hint at the bottom reads: "You can view and manage it in the agent list after creation" (创建后可在智能体列表中查看和管理). **The Create agent button becomes clickable only after you enter a name.**

## ⏰ Scheduled

> Runs tasks automatically on a schedule. Set the task and frequency, and the agent runs on plan — no manual trigger needed.

<Shot src="/media/zh/agent-new-scheduled.png" caption="Scheduled type" />

| Field | Required | Description / example |
| --- | --- | --- |
| Agent name (智能体名称) | Optional | A name is generated if left blank |
| Task description (任务描述) | ✅ | Describe the work the agent should do on a recurring basis |
| Run frequency (运行频率) | — | Defaults to "Every 30 minutes" (每 30 分钟) |

Available frequencies:

| Every 1 minute | Every 5 minutes | Every 30 minutes (default) | Every hour | Every 3 hours | Every 6 hours |
| :-: | :-: | :-: | :-: | :-: | :-: |

::: warning
The hint at the bottom reads: **"It must be started after creation to run on schedule."** (创建后需启动才会按计划自动跑。) Don't forget to start it once it's created.
:::

## ⚡ Event-triggered

> Responds automatically when new objects appear. Choose the object types you care about, tell the agent what to do when it finds one, and it handles the rest.

<Shot src="/media/zh/agent-new-event.png" caption="Event-triggered type" />

| Field | Required | Description / example |
| --- | --- | --- |
| Agent name (智能体名称) | Optional | If left blank, it's named "Object · Follow-up" (对象 · 跟进) |
| Objects to watch (你想关注的对象) | ✅ | Filter with the search box first (e.g. VIP, visitor, alert), then click **Select** (选择) on the right of each row. **Multiple selections allowed — any one appearing triggers the agent** |
| What to do when found (发现后要做什么) | ✅ | e.g. Automatically summarize the key information and notify me. A live preview below reads "When *your selected objects* appear, the agent will automatically: …" |

Object types currently available (the platform's list is the source of truth):

<Kv :rows="[
  ['Space', 'enclosure · origin · space.structure · space.zone'],
  ['Camera', 'camera · camera.info'],
  ['Shape', 'shape · rectangle'],
  ['Rendering', 'render · render.config · render.layer · render.space · render.model · render.material · render.3dgs'],
  ['Render transform', 'render.offset · render.rotation · render.scale · render.keyFrames'],
  ['Environment', 'render.ambientLight · skybox'],
]" />

::: tip
The **Create agent** button stays disabled until you've **selected at least one object** and **filled in "What to do when found"**.
:::
