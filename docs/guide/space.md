# 空间与切换

**空间**是 Spatial Smart 中最顶层的容器。应用会话、智能体、服务都属于某一个空间。切换空间后，三个模块的内容都会随之切换。

::: warning 先选空间，再干活
未选择空间时，「新建智能体」「新建服务」、输入框的附件等按钮都是灰色不可用的，并会看到「请先在顶部选择空间，再查看或新建智能体。」之类的提示。
:::

<Shot src="/media/zh/agent-no-space.png" caption="未选择空间时：按钮置灰，并提示先选择空间" />

## 选择空间

<Shot src="/media/zh/shell-space-picker.png" caption="空间下拉列表：每一项显示空间名称和 UUID，右侧可复制 ID" />

::: steps
1. 点击左上角的 **「请选择空间...」**。
2. 选择器变成搜索框，下方展开「选择空间」列表。
3. 输入空间名称的一部分即可实时过滤（子串匹配）。
4. 点击目标空间。选择器显示空间名称，三大模块刷新为该空间的内容。
:::

<Demo src="/media/zh/flow-switch-space-and-modules.mp4" caption="选择空间并在模块之间切换" />

## 小技巧

- **复制空间 ID**：列表中每个空间名下方是灰色的 UUID，旁边的复制图标可一键复制，向同事或管理员反馈问题时很有用。
- **用链接直达空间**：选中空间后，地址栏会带上 `encId=<空间ID>&spaceName=<空间名>`。把这个链接发给同事，对方打开后直接进入同一空间。
- **配合模块参数**：再加上 `module=agent` 或 `module=service` 可以直达对应模块，例如 `?module=service&encId=...`。

| 地址参数 | 含义 | 示例 |
| --- | --- | --- |
| `module` | 打开的模块：`app`（默认）、`agent`、`service` | `module=agent` |
| `encId` | 空间 ID | `encId=37143acf-…` |
| `spaceName` | 空间名称（URL 编码） | `spaceName=%5B…%5D` |

::: danger 注意
名称带有 **[勿删]** 的空间通常是团队共用或测试用空间，请不要删除其中的内容。
:::
