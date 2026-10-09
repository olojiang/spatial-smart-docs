# Spaces

A **space** is the top-level container in Spatial Smart. App conversations, agents, and services all belong to a space. When you switch spaces, the content of all three modules switches with it.

::: warning Select a space before you start
With no space selected, buttons such as **New agent** (新建智能体), **New service** (新建服务), and the input box's attachment button are grayed out, and you'll see a hint like "Select a space at the top before viewing or creating agents." (请先在顶部选择空间，再查看或新建智能体。)
:::

<Shot src="/media/zh/agent-no-space.png" caption="No space selected: buttons are grayed out with a prompt to select a space" />

## Select a space

<Shot src="/media/zh/shell-space-picker.png" caption="Space dropdown: each entry shows the space name and UUID, with a copy-ID button on the right" />

::: steps
1. Click **"Select a space..."** (请选择空间...) in the top-left corner.
2. The picker turns into a search box, and the **Select space** (选择空间) list opens below it.
3. Type part of a space name to filter in real time (substring match).
4. Click the space you want. The picker shows its name, and all three modules refresh with that space's content.
:::

<Demo src="/media/zh/flow-switch-space-and-modules.mp4" caption="Select a space and switch between modules" />

## Tips

- **Copy the space ID**: below each space name in the list is a gray UUID with a copy icon next to it — handy when reporting an issue to a colleague or administrator.
- **Link straight to a space**: once a space is selected, the address bar includes `encId=<space ID>&spaceName=<space name>`. Share that link and your colleague lands in the same space.
- **Add a module parameter**: append `module=agent` or `module=service` to jump to that module, e.g. `?module=service&encId=...`.

| URL parameter | Meaning | Example |
| --- | --- | --- |
| `module` | Module to open: `app` (default), `agent`, `service` | `module=agent` |
| `encId` | Space ID | `encId=37143acf-…` |
| `spaceName` | Space name (URL-encoded) | `spaceName=%5B…%5D` |

::: danger Caution
Spaces whose names contain **[勿删]** ("do not delete") are usually shared team or test spaces. Don't delete anything in them.
:::
