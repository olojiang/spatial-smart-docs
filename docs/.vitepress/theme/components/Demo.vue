<script setup lang="ts">
/** Autoplaying, looping muted demo clip (mp4/webm) or GIF, framed like <Shot>. */
import { withBase } from 'vitepress'
defineProps<{ src: string; caption?: string; poster?: string }>()
</script>
<template>
  <figure class="ssd-demo">
    <img v-if="src.endsWith('.gif')" :src="withBase(src)" :alt="caption" loading="lazy" />
    <video v-else :src="withBase(src)" :poster="poster && withBase(poster)" autoplay loop muted playsinline controls />
    <figcaption v-if="caption">▶ {{ caption }}</figcaption>
  </figure>
</template>
<style scoped>
.ssd-demo { margin: 24px 0; } .ssd-demo img, .ssd-demo video { width: 100%; border-radius: 12px; border: 1px solid var(--vp-c-divider); box-shadow: 0 10px 40px -12px var(--ssd-glow); }
figcaption { text-align: center; font-size: 13px; color: var(--vp-c-text-2); margin-top: 10px; }
</style>
