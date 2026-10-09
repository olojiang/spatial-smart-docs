# Spatial Smart 使用手册 · User Manual

> 松田 **Spatial Smart**（[alpha.pinefield.cn/pinefield.spatial-smart](https://alpha.pinefield.cn/pinefield.spatial-smart/)）的完整中英双语使用手册。
> A complete bilingual (中文 / English) user manual for Pinefield Spatial Smart.

- 📚 覆盖登录、界面、空间、应用（对话开发）、智能体、服务（API）、设置全部功能
- 🖼️ 30+ 张真实截图、4 段操作短视频、Mermaid 流程图
- 🔍 全站搜索 · 侧边栏 + 页内目录导航
- 🎨 7 套主题：专业 / 浅色 / 深色 / 护眼 / 黑金 / 墨绿 / 暖橙（右上角切换，自动记住）
- 🤖 截图、录屏、站点巡检全部脚本化，站点更新后可一键重拍并比对差异

## 快速开始

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # 输出到 docs/.vitepress/dist
npm run check      # 中英文页面对齐 + 资源完整性检查
```

## 目录结构

```
docs/
  *.md, guide/ apps/ agents/ services/ settings/ reference/   中文（默认语言）
  en/                                                         English（与中文同名同路径）
  public/media/zh/                                            截图与短视频
  .vitepress/
    config.mts        站点配置（语言、搜索、Mermaid）
    sidebar.ts        ★ 导航唯一来源：一处定义，中英文侧边栏同时生成
    theme/
      themes.ts       ★ 主题注册表（新增主题：这里加一项 + themes.css 加一段）
      themes.css      7 套主题的 CSS 变量
      custom.css      全局动效与排版
      components/     Shot（截图框+标注+放大）、Demo（短视频）、Kv、FeatureGrid、ThemeSwitcher
tools/capture/        Playwright 自动登录、截图、录屏、站点快照
scripts/              check-parity.mjs、snapshot-diff.mjs
snapshot/sitemap.json 站点功能快照（用于检测站点更新）
```

## 写作组件

```md
<Shot src="/media/zh/service-overview.png" caption="说明" marks="10,30,1|38,25,2" />
<Demo src="/media/zh/flow-service-workbench.mp4" caption="说明" />

::: steps
1. 第一步
2. 第二步
:::
```

`marks` 为 `x%,y%,序号`，用 `|` 分隔，会在截图上画出带脉冲动画的编号标注。

## 文档维护

- 新增页面、修改主题、写作规范：见 [CONTRIBUTING.md](CONTRIBUTING.md)
- **站点更新后如何同步文档**：见 [UPDATING.md](UPDATING.md)

## 部署

推送到 `main` 后 Vercel 自动构建部署（配置见 `vercel.json`）。GitHub Actions 在每次推送时运行对齐检查与构建。
