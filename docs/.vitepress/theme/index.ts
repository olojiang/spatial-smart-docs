/**
 * Theme entry: extends the VitePress default theme with
 *  - the 7-theme switcher in the nav bar
 *  - global doc components (<Shot>, <Demo>, <Steps>, <FeatureGrid>, <Kv>)
 */
import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import ThemeSwitcher from './components/ThemeSwitcher.vue'
import Shot from './components/Shot.vue'
import Demo from './components/Demo.vue'
import FeatureGrid from './components/FeatureGrid.vue'
import Kv from './components/Kv.vue'
import './themes.css'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, {
    'nav-bar-content-after': () => h(ThemeSwitcher),
  }),
  enhanceApp({ app }) {
    app.component('Shot', Shot)
    app.component('Demo', Demo)
    app.component('FeatureGrid', FeatureGrid)
    app.component('Kv', Kv)
  },
} satisfies Theme
