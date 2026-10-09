# Start a conversation

**Apps** (应用) is Spatial Smart's default module: describe what you need in plain language, and AI writes code, explains your project, and generates pages inside a **workspace**. Think of it as an engineer sitting right next to you.

<Shot src="/media/zh/app-home.png" caption="Apps home: “Spatial intelligence, now at your fingertips” (从现在起，空间智能触手可及)" marks="5,13,1|51,48,2|42,58,3|47,58,4|80,58,5|84,58,6|87.5,58,7" />

| # | Control | Description |
| --- | --- | --- |
| 1 | **New conversation** (新对话) | Starts a brand-new conversation |
| 2 | **Input box** | Describe what you need; on the home screen the placeholder reads "Search workspaces, create a workspace, connect a data source... describe what you need" (搜索工作空间、创建工作空间、连接数据源... 请描述您的需求) |
| 3 | **Workspace** (工作空间) | Choose the workspace for the conversation, or **＋ New** (＋ 新建) |
| 4 | **Attachment (📎)** | Attach files; grayed out while the input is empty |
| 5 | **Model** | The current model, *Kimi K2.6* by default |
| 6 | **Web search (🌐)** (联网) | Lets the AI search the web; **on by default** (highlighted in blue) |
| 7 | **Send** | Available once you've typed something; turns into **■ Stop** (停止) while generating |

## Send your first message

<Demo src="/media/zh/flow-app-chat.mp4" caption="Type a request → press Enter → the AI streams its reply and the code workbench opens on the right" />

::: steps
1. (Optional) Select a space in the top-left corner first, then choose or create a workspace from the **Workspace** menu.
2. Type your request in the input box, such as "What can you help me with?". Press <kbd>Enter</kbd> to send.
3. Your message appears at the top right; a blue ✦ loading animation appears below it, and **the Send button turns into a square Stop button** so you can interrupt generation at any time.
4. The **code workbench** opens on the right, first showing "Loading file tree…" (正在加载文件树…), then the project files. → [Code workbench](/en/apps/workbench)
5. The reply includes a collapsible **Thinking complete** (思考完成) marker — expand it to see the model's reasoning.
6. When the reply finishes, the conversation is named after your first message and appears in the list on the left.
:::

<Shot src="/media/zh/app-conversation.png" caption="A complete conversation: conversation list on the left, reply in the middle, code workbench on the right" />

## Shortcuts for follow-up messages

Once the conversation starts, the input placeholder changes to: `输入消息... (@ 引用文件, / Slash Commands, $ Shortcut)...` (Type a message... (@ reference files, / Slash Commands, $ Shortcut)...)

| Input | What it does | Example |
| --- | --- | --- |
| `@` | Reference a file in the workspace so the AI focuses on it | `@src/App.tsx 这里为什么报错？` (Why does this throw an error?) |
| `/` | Run a slash command or an enabled Skill | `/skill-name` |
| `$` | Use a shortcut | Type `$` and follow the prompt |

::: tip 3 keys to a good request
1. **State the goal**: what page, endpoint, or feature you want.
2. **Provide the data**: fields, sample values, and data sources.
3. **Define acceptance criteria**: e.g. "run the tests when you're done."
:::

## Choose a model

Click the model name below the input box to open the model list. You can **search models** at the top or narrow the list with the **Filter** (筛选) button; the current model is highlighted.

<Shot src="/media/zh/app-model-picker.png" caption="Model picker: search and filter" />

The 20 models currently available:

| Vendor / family | Models |
| --- | --- |
| ByteDance Doubao | Doubao Seed Code |
| MiniMax | MiniMax M3 |
| Moonshot Kimi | Kimi K2.6 (default), Kimi K2.7 Code, Kimi K3 |
| OpenAI GPT | GPT-5.2, GPT-5.2 Codex, GPT-5.3 Codex, GPT-5.4, GPT-5.5, GPT-5.6-luna, GPT-5.6-sol, GPT-5.6-terra |
| DeepSeek | DeepSeek V4 Flash, DeepSeek V4 Pro |
| Zhipu GLM | GLM 5.1, GLM 5.2, GLM 5.3, GLM 5.3 Flash |

::: info Which one should I pick?
For coding, prefer models with **Code / Codex** in the name; for speed, pick **Flash**; for general Q&A, the default Kimi K2.6 is fine. The platform's model list is the source of truth.
:::

## Workspace menu

Click **New workspace ⌄** (新工作空间 ⌄) below the input box. The top half lists **Recent workspaces** (最近工作空间) — or "No recent workspaces" (暂无最近工作空间) if there are none — and the bottom half has **＋ New** (＋ 新建).

<Shot src="/media/zh/app-workspace-menu.png" caption="Workspace menu: recent workspaces + New" />

## Manage conversations

- **Conversation list**: under the **Apps** group on the left, conversations are grouped by workspace (e.g. **Default** (默认)). Click one to reopen it; the **＋** at the right of each workspace row starts a new conversation in it.
- **Conversation menu**: the **⋯** next to a conversation title offers **Rename conversation** (重命名会话) and **Conversation settings** (会话设置).
- **New conversation**: **New conversation** (新对话) at the top of the left pane starts a new topic anytime.

::: warning Note
If no space is selected, new conversations go into the **Default** workspace. If you're working in a particular space, select it first.
:::
