<script setup lang="ts">
/** Key-value fact sheet (borrowed from answer-me-with-html's `kv`). rows: [[key, value], ...] */
defineProps<{ rows: [string, string][] }>()
</script>
<template>
  <dl class="ssd-kv"><template v-for="[k, v] in rows" :key="k"><dt>{{ k }}</dt><dd v-html="v" /></template></dl>
</template>
<style scoped>
.ssd-kv { display: grid; grid-template-columns: max-content 1fr; gap: 0; border: 1px solid var(--vp-c-divider); border-radius: 12px; overflow: hidden; margin: 20px 0; }
dt, dd { margin: 0; padding: 10px 16px; border-bottom: 1px solid var(--vp-c-divider); font-size: 14px; }
dt { background: var(--vp-c-bg-soft); color: var(--vp-c-text-2); font-weight: 600; }
dt:nth-last-of-type(1), dd:last-of-type { border-bottom: 0; }
</style>
