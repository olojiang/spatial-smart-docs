# 贡献指南

## 新增一个页面

1. 在 `docs/.vitepress/sidebar.ts` 对应分组中加一项：`{ slug: 'agents/xxx', text: { zh: '中文标题', en: 'English Title' } }`
2. 新建 `docs/agents/xxx.md`（中文）与 `docs/en/agents/xxx.md`（英文）。
3. `npm run check && npm run build`，两者都通过再提交。

## 写作规范

- **先概念、后操作、再细节**：页面开头一句话说清「这是什么、什么时候用」，再给 `::: steps` 步骤，最后是字段表与注意事项。
- 步骤用短句、祈使句，一步只做一件事。
- 界面上的文字用 **粗体** 并与界面保持完全一致；英文页写作 **English label**（中文标签）。
- 每个操作页至少一张 `<Shot>`；多步交互优先用 `<Demo>` 短视频。
- 提示用 `::: tip`，风险用 `::: warning`，不可逆操作用 `::: danger`。
- 图表用 Mermaid；配色已在 `config.mts` 统一，**不要使用紫色/靛蓝**。

## 新增主题

1. `docs/.vitepress/theme/themes.ts` 的 `THEMES` 数组加一项（id、中英文名、两个色块、是否深色）。
2. `docs/.vitepress/theme/themes.css` 加 `:root[data-theme='id'] { ... }` 一段变量。

## 截图与短视频

见 [UPDATING.md](UPDATING.md)。
