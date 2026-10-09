import { defineConfig, type DefaultTheme } from 'vitepress'
import { withMermaid } from 'vitepress-plugin-mermaid'
import container from 'markdown-it-container'
import { sections, type Lang } from './sidebar'

const SITE_URL = 'https://alpha.pinefield.cn/pinefield.spatial-smart/'

/** Build a VitePress sidebar for one language from the shared nav config. */
function sidebarFor(lang: Lang): DefaultTheme.SidebarItem[] {
  const prefix = lang === 'zh' ? '/' : '/en/'
  return sections.map((s) => ({
    text: s.text[lang],
    collapsed: false,
    items: s.items.map((i) => ({ text: i.text[lang], link: prefix + i.slug })),
  }))
}

export default withMermaid(
  defineConfig({
    title: 'Spatial Smart Docs',
    cleanUrls: true,
    lastUpdated: true,
    head: [['link', { rel: 'icon', href: '/logo.svg' }]],
    themeConfig: {
      logo: '/logo.svg',
      search: {
        provider: 'local',
        options: {
          locales: {
            root: {
              translations: {
                button: { buttonText: '搜索文档', buttonAriaLabel: '搜索文档' },
                modal: {
                  noResultsText: '没有找到相关结果',
                  resetButtonTitle: '清除查询',
                  footer: { selectText: '选择', navigateText: '切换', closeText: '关闭' },
                },
              },
            },
          },
        },
      },
    },
    locales: {
      root: {
        label: '简体中文',
        lang: 'zh-CN',
        title: 'Spatial Smart 使用手册',
        description: '松田 Spatial Smart 空间智能平台完整使用指南',
        themeConfig: {
          nav: [
            { text: '指南', link: '/guide/overview' },
            { text: '常见问题', link: '/reference/faq' },
            { text: '更新日志', link: '/changelog' },
            { text: '打开平台', link: SITE_URL },
          ],
          sidebar: sidebarFor('zh'),
          outline: { label: '本页目录', level: [2, 3] },
          docFooter: { prev: '上一页', next: '下一页' },
          lastUpdated: { text: '最后更新' },
          darkModeSwitchLabel: '外观',
          returnToTopLabel: '回到顶部',
          sidebarMenuLabel: '菜单',
        },
      },
      en: {
        label: 'English',
        lang: 'en-US',
        link: '/en/',
        title: 'Spatial Smart Manual',
        description: 'The complete user guide to Pinefield Spatial Smart',
        themeConfig: {
          nav: [
            { text: 'Guide', link: '/en/guide/overview' },
            { text: 'FAQ', link: '/en/reference/faq' },
            { text: 'Changelog', link: '/en/changelog' },
            { text: 'Open the app', link: SITE_URL },
          ],
          sidebar: sidebarFor('en'),
          outline: { level: [2, 3] },
        },
      },
    },
    markdown: {
      // `::: steps` wraps an ordered list into a numbered timeline (see custom.css)
      config: (md) => { md.use(container, 'steps') },
    },
    // Diagram layout: generous padding/spacing; label text styles are reset in
    // custom.css so measured boxes always fit (no clipped text). Colors come from the active site theme via
    // CSS variables in custom.css, so diagrams follow all 7 themes.
    mermaid: {
      theme: 'base',
      themeVariables: { edgeLabelBackground: 'transparent', fontFamily: 'Inter, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif', fontSize: '15px' },
      flowchart: { padding: 22, nodeSpacing: 56, rankSpacing: 64, diagramPadding: 20, curve: 'basis', useMaxWidth: true },
      state: { padding: 16 },
    },
  }),
)
