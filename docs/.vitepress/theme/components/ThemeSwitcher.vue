<script setup lang="ts">
/**
 * "切换主题" dropdown. Persists choice in localStorage and keeps VitePress's
 * own dark-mode class in sync with the selected theme.
 */
import { ref, onMounted, computed } from 'vue'
import { useData } from 'vitepress'
import { THEMES, DEFAULT_THEME, STORAGE_KEY } from '../themes'

const { lang, isDark } = useData()
const open = ref(false)
const current = ref(DEFAULT_THEME)
const isZh = computed(() => lang.value.startsWith('zh'))

function apply(id: string) {
  const t = THEMES.find((x) => x.id === id) ?? THEMES[0]
  current.value = t.id
  document.documentElement.dataset.theme = t.id
  isDark.value = t.dark
  localStorage.setItem(STORAGE_KEY, t.id)
  open.value = false
}

onMounted(() => apply(localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME))
</script>

<template>
  <div class="ssd-theme" @keydown.esc="open = false">
    <button class="ssd-theme-btn" :aria-label="isZh ? '切换主题' : 'Switch theme'" @click="open = !open">
      <span class="dot" :style="{ '--a': THEMES.find(t => t.id === current)?.swatch[0], '--b': THEMES.find(t => t.id === current)?.swatch[1] }" />
      <svg width="12" height="12" viewBox="0 0 24 24"><path fill="currentColor" d="M7 10l5 5 5-5z" /></svg>
    </button>
    <Transition name="pop">
      <div v-if="open" class="ssd-theme-menu" role="menu">
        <div class="title">{{ isZh ? '切换主题' : 'Theme' }}</div>
        <button v-for="t in THEMES" :key="t.id" class="item" role="menuitemradio"
          :aria-checked="t.id === current" @click="apply(t.id)">
          <span class="dot" :style="{ '--a': t.swatch[0], '--b': t.swatch[1] }" />
          <span class="name">{{ isZh ? t.label.zh : t.label.en }}</span>
          <span v-if="t.id === current" class="check">✓</span>
        </button>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.ssd-theme { position: relative; margin-left: 12px; display: flex; align-items: center; }
.ssd-theme-btn { display: flex; gap: 4px; align-items: center; padding: 4px 6px; border-radius: 20px;
  border: 1px solid var(--vp-c-divider); color: var(--vp-c-text-2); }
.dot { width: 18px; height: 18px; border-radius: 50%; border: 1px solid var(--vp-c-divider);
  background: linear-gradient(135deg, var(--a) 50%, var(--b) 50%); flex: none; }
.ssd-theme-menu { position: absolute; right: 0; top: 40px; min-width: 180px; padding: 8px;
  background: var(--vp-c-bg-elv); border: 1px solid var(--vp-c-divider); border-radius: 14px;
  box-shadow: 0 18px 50px rgba(0,0,0,.25); z-index: 100; backdrop-filter: blur(12px); }
.title { font-size: 12px; color: var(--vp-c-text-3); padding: 4px 10px 8px; }
.item { display: flex; align-items: center; gap: 12px; width: 100%; padding: 8px 10px; border-radius: 10px;
  font-size: 14px; color: var(--vp-c-text-1); text-align: left; }
.item:hover { background: var(--vp-c-brand-soft); }
.name { flex: 1; }
.check { color: var(--vp-c-brand-1); }
.pop-enter-active, .pop-leave-active { transition: all .16s ease; }
.pop-enter-from, .pop-leave-to { opacity: 0; transform: translateY(-6px) scale(.98); }
</style>
