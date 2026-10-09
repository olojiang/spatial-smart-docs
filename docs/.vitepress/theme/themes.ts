/**
 * Theme registry. Each theme is a set of CSS variables defined in themes.css
 * under [data-theme="<id>"]. To add a theme: add an entry here and a block in themes.css.
 */
export interface ThemeDef {
  id: string
  label: { zh: string; en: string }
  /** two swatch colors shown in the switcher (background, accent) */
  swatch: [string, string]
  /** whether the theme is dark (drives VitePress .dark class) */
  dark: boolean
}

export const THEMES: ThemeDef[] = [
  { id: 'pro', label: { zh: '专业', en: 'Professional' }, swatch: ['#ffffff', '#1a7f9c'], dark: false },
  { id: 'light', label: { zh: '浅色', en: 'Light' }, swatch: ['#ffffff', '#1f1f1f'], dark: false },
  { id: 'dark', label: { zh: '深色', en: 'Dark' }, swatch: ['#0b0d10', '#22d3ee'], dark: true },
  { id: 'eye', label: { zh: '护眼', en: 'Eye Care' }, swatch: ['#f3efdc', '#4f7a5a'], dark: false },
  { id: 'blackgold', label: { zh: '黑金', en: 'Black Gold' }, swatch: ['#121212', '#c9a560'], dark: true },
  { id: 'ink', label: { zh: '墨绿', en: 'Ink Green' }, swatch: ['#ffffff', '#1e6b3c'], dark: false },
  { id: 'orange', label: { zh: '暖橙', en: 'Warm Orange' }, swatch: ['#ffffff', '#ea580c'], dark: false },
]

export const DEFAULT_THEME = 'pro'
export const STORAGE_KEY = 'ssd-theme'
