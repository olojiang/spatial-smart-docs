# 站点更新后如何同步文档

Spatial Smart 迭代很快。本仓库把「发现变化 → 更新截图 → 修改文档」做成了可重复的流程。

```
tools/capture/
  browser.py    自动登录（含验证码识别），会话缓存在 .auth/（已 git-ignore）
  scenes.py     ★ 所有截图的声明式清单：名称 + 地址 + 操作步骤
  capture.py    按 scenes.py 重拍截图 → docs/public/media/zh/*.png
  flows.py      ★ 短视频的操作脚本
  record.py     按 flows.py 录制 → docs/public/media/zh/*.mp4
  snapshot.py   爬取每个模块可见的按钮/标签/输入框 → snapshot/sitemap.new.json
  dump.py       调试：列出某页所有 data-testid
```

## 0. 一次性准备

```bash
./tools/capture/setup.sh                 # 安装 playwright、ddddocr、浏览器
export SS_USER=你的账号 SS_PASSWORD=你的密码   # 只放在环境变量里，切勿提交
```

## 1. 发现变化

```bash
python3 tools/capture/snapshot.py        # 生成 snapshot/sitemap.new.json
npm run diff:snapshot                    # 与已提交的 snapshot/sitemap.json 比对
```

输出示例：

```
~ 服务 › 服务工作区  → docs: services/workbench
  + tabs: 监控
  - actions: 标记为不可用
+ NEW PAGE 数据源  (?module=datasource)
```

每一处变化都标出了**需要修改的文档页**。

## 2. 更新截图与视频

```bash
python3 tools/capture/capture.py               # 全部重拍
python3 tools/capture/capture.py service-      # 只重拍以 service- 开头的
python3 tools/capture/record.py flow-service   # 重录某段视频
```

某个场景失败（✗）通常是界面上的按钮文字或 testid 变了：用 `python3 tools/capture/dump.py "?module=service"` 查新的选择器，改 `scenes.py` 后重跑。

## 3. 修改文档

- 按 diff 列出的页面，同时修改 `docs/<页面>.md` 与 `docs/en/<页面>.md`。
- 新功能：新建页面并加入 `sidebar.ts`（见 CONTRIBUTING.md）。
- 删除的功能：删除对应段落与截图，`npm run check` 会提示失效的资源引用。

## 4. 记录并发布

1. 在 `docs/changelog.md` 与 `docs/en/changelog.md` 顶部加一条：日期、变化摘要、最后核对日期。
2. `cp snapshot/sitemap.new.json snapshot/sitemap.json`（把新快照设为基准）。
3. `npm run check && npm run build`，提交并推送，Vercel 自动重新部署。
