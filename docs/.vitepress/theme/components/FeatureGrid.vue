<script setup lang="ts">
/** Card grid linking to modules. items: [{ icon, title, desc, link }] */
import { withBase } from 'vitepress'
defineProps<{ items: { icon: string; title: string; desc: string; link?: string }[] }>()
</script>
<template>
  <div class="ssd-grid">
    <a v-for="(it, i) in items" :key="it.title" class="card" :href="it.link ? withBase(it.link) : undefined" :style="{ animationDelay: i * 60 + 'ms' }">
      <div class="icon">{{ it.icon }}</div><h4>{{ it.title }}</h4><p>{{ it.desc }}</p>
    </a>
  </div>
</template>
<style scoped>
.ssd-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 16px; margin: 24px 0; }
.card { display: block; padding: 20px; border-radius: 14px; border: 1px solid var(--vp-c-divider); background: var(--vp-c-bg-soft);
  text-decoration: none !important; color: inherit !important; transition: transform .25s, border-color .25s, box-shadow .25s;
  animation: rise .5s both; }
.card:hover { transform: translateY(-4px); border-color: var(--vp-c-brand-1); box-shadow: 0 16px 40px -18px var(--ssd-glow); }
.icon { font-size: 26px; width: 48px; height: 48px; display: grid; place-items: center; border-radius: 12px; background: var(--vp-c-brand-soft); margin-bottom: 12px; }
h4 { margin: 0 0 6px; font-size: 16px; } p { margin: 0; font-size: 13px; color: var(--vp-c-text-2); line-height: 1.6; }
@keyframes rise { from { opacity: 0; transform: translateY(12px); } }
</style>
