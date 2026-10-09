#!/usr/bin/env node
/**
 * Fails (exit 1) when the zh and en doc trees diverge:
 *  - a page listed in sidebar.ts is missing in either language
 *  - a markdown file exists in one language but not the other
 *  - a referenced /media/* asset does not exist
 */
import { readFileSync, existsSync, readdirSync, statSync } from 'node:fs'
import { join, relative } from 'node:path'

const DOCS = 'docs'
const errors = []

// 1. every sidebar slug exists in both languages
const sidebarSrc = readFileSync(join(DOCS, '.vitepress/sidebar.ts'), 'utf8')
const slugs = [...sidebarSrc.matchAll(/slug:\s*'([^']+)'/g)].map((m) => m[1])
for (const slug of slugs) {
  for (const base of [DOCS, join(DOCS, 'en')]) {
    if (!existsSync(join(base, slug + '.md'))) errors.push(`missing page: ${join(base, slug)}.md`)
  }
}

// 2. file trees mirror each other
const walk = (dir) => readdirSync(dir).flatMap((f) => {
  const p = join(dir, f)
  if (f.startsWith('.') || f === 'public' || (dir === DOCS && f === 'en')) return []
  return statSync(p).isDirectory() ? walk(p) : f.endsWith('.md') ? [p] : []
})
const zh = new Set(walk(DOCS).map((p) => relative(DOCS, p)))
const en = new Set(walk(join(DOCS, 'en')).map((p) => relative(join(DOCS, 'en'), p)))
for (const f of zh) if (!en.has(f)) errors.push(`no English counterpart: ${f}`)
for (const f of en) if (!zh.has(f)) errors.push(`no Chinese counterpart: ${f}`)

// 3. media references resolve
for (const f of [...zh].map((p) => join(DOCS, p)).concat([...en].map((p) => join(DOCS, 'en', p)))) {
  for (const m of readFileSync(f, 'utf8').matchAll(/["'(](\/media\/[^"')\s]+)/g)) {
    if (!existsSync(join(DOCS, 'public', m[1]))) errors.push(`${f}: missing asset ${m[1]}`)
  }
}

if (errors.length) { console.error('✗ parity check failed:\n  ' + errors.join('\n  ')); process.exit(1) }
console.log(`✓ ${slugs.length} sidebar pages, ${zh.size} zh / ${en.size} en files, all assets present`)
