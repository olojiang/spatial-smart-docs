/**
 * Single source of truth for navigation.
 * Each entry declares its zh/en titles once; config.mts generates both
 * language sidebars from this file. To add a page:
 *   1. add an item here (slug = file path without .md)
 *   2. create docs/<slug>.md (zh) and docs/en/<slug>.md (en)
 *   `npm run check` fails if either language file is missing.
 */
export type Lang = 'zh' | 'en'
export interface NavItem { slug: string; text: Record<Lang, string> }
export interface NavSection { text: Record<Lang, string>; items: NavItem[] }

export const sections: NavSection[] = [
  {
    text: { zh: '快速入门', en: 'Getting Started' },
    items: [
      { slug: 'guide/overview', text: { zh: '产品概览', en: 'Overview' } },
      { slug: 'guide/quickstart', text: { zh: '5 分钟上手', en: '5-Minute Quickstart' } },
      { slug: 'guide/login', text: { zh: '登录与退出', en: 'Sign In & Out' } },
      { slug: 'guide/interface', text: { zh: '界面导览', en: 'Interface Tour' } },
      { slug: 'guide/space', text: { zh: '空间与切换', en: 'Spaces' } },
    ],
  },
  {
    text: { zh: '应用 · 对话开发', en: 'Apps · Chat to Build' },
    items: [
      { slug: 'apps/chat', text: { zh: '发起对话', en: 'Start a Conversation' } },
      { slug: 'apps/workbench', text: { zh: '代码工作台', en: 'Code Workbench' } },
    ],
  },
  {
    text: { zh: '智能体', en: 'Agents' },
    items: [
      { slug: 'agents/overview', text: { zh: '智能体概览', en: 'Agents Overview' } },
      { slug: 'agents/create', text: { zh: '新建智能体', en: 'Create an Agent' } },
      { slug: 'agents/manage', text: { zh: '配置与试运行', en: 'Configure & Test' } },
    ],
  },
  {
    text: { zh: '服务', en: 'Services' },
    items: [
      { slug: 'services/overview', text: { zh: '服务概览', en: 'Services Overview' } },
      { slug: 'services/create', text: { zh: '新建 API 服务', en: 'Create an API Service' } },
      { slug: 'services/workbench', text: { zh: '服务工作区', en: 'Service Workbench' } },
    ],
  },
  {
    text: { zh: '个人与设置', en: 'Account & Settings' },
    items: [
      { slug: 'settings/preferences', text: { zh: '偏好设置', en: 'Preferences' } },
      { slug: 'settings/usage-feedback', text: { zh: '用量与反馈', en: 'Usage & Feedback' } },
      { slug: 'settings/appearance', text: { zh: '语言与外观', en: 'Language & Appearance' } },
    ],
  },
  {
    text: { zh: '参考', en: 'Reference' },
    items: [
      { slug: 'reference/faq', text: { zh: '常见问题', en: 'FAQ' } },
      { slug: 'reference/glossary', text: { zh: '术语表', en: 'Glossary' } },
    ],
  },
]
