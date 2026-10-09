<script setup lang="ts">
/** Screenshot with browser-window frame, caption, optional hotspot markers and click-to-zoom. */
import { ref } from 'vue'
import { withBase } from 'vitepress'
const props = defineProps<{ src: string; caption?: string; url?: string
  /** markers: "x,y,label" in percent, separated by | e.g. "12,30,1|60,40,2" */
  marks?: string }>()
const zoom = ref(false)
const markers = (props.marks ?? '').split('|').filter(Boolean).map((m) => {
  const [x, y, label] = m.split(','); return { x, y, label }
})
</script>
<template>
  <figure class="ssd-shot">
    <div class="frame" @click="zoom = true">
      <div class="bar"><i /><i /><i /><span>{{ url ?? 'alpha.pinefield.cn' }}</span></div>
      <div class="pic">
        <img :src="withBase(src)" :alt="caption" loading="lazy" />
        <b v-for="m in markers" :key="m.label" class="mark" :style="{ left: m.x + '%', top: m.y + '%' }">{{ m.label }}</b>
      </div>
    </div>
    <figcaption v-if="caption">{{ caption }}</figcaption>
    <Teleport to="body">
      <Transition name="fade"><div v-if="zoom" class="ssd-lightbox" @click="zoom = false"><img :src="withBase(src)" :alt="caption" /></div></Transition>
    </Teleport>
  </figure>
</template>
<style scoped>
.ssd-shot { margin: 24px 0; }
.frame { border: 1px solid var(--vp-c-divider); border-radius: 12px; overflow: hidden; cursor: zoom-in;
  box-shadow: 0 10px 40px -12px var(--ssd-glow); transition: transform .25s, box-shadow .25s; background: var(--vp-c-bg-soft); }
.frame:hover { transform: translateY(-3px); box-shadow: 0 20px 60px -15px var(--ssd-glow); }
.bar { display: flex; align-items: center; gap: 6px; padding: 8px 12px; border-bottom: 1px solid var(--vp-c-divider); }
.bar i { width: 10px; height: 10px; border-radius: 50%; background: #ff5f57; } .bar i:nth-child(2){background:#febc2e} .bar i:nth-child(3){background:#28c840}
.bar span { margin-left: 10px; font-size: 12px; color: var(--vp-c-text-3); }
.pic { position: relative; } .pic img { display: block; width: 100%; }
.mark { position: absolute; transform: translate(-50%,-50%); width: 26px; height: 26px; border-radius: 50%;
  background: var(--vp-c-brand-1); color: #fff; font-size: 13px; display: grid; place-items: center;
  box-shadow: 0 0 0 4px var(--vp-c-brand-soft); animation: pulse 2s infinite; }
@keyframes pulse { 50% { box-shadow: 0 0 0 10px transparent; } }
figcaption { text-align: center; font-size: 13px; color: var(--vp-c-text-2); margin-top: 10px; }
.ssd-lightbox { position: fixed; inset: 0; z-index: 999; background: rgba(0,0,0,.8); display: grid; place-items: center; cursor: zoom-out; padding: 4vw; }
.ssd-lightbox img { max-width: 100%; max-height: 100%; border-radius: 10px; }
.fade-enter-active,.fade-leave-active{transition:opacity .2s}.fade-enter-from,.fade-leave-to{opacity:0}
</style>
