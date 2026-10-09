#!/usr/bin/env node
/**
 * Compare two site snapshots and print what changed, grouped per page.
 * Usage: node scripts/snapshot-diff.mjs [old=snapshot/sitemap.json] [new=snapshot/sitemap.new.json]
 *
 * Snapshot format (see UPDATING.md):
 * { "capturedAt": "...", "pages": [ { "id", "menuPath": [..], "url", "docs": ["guide/x"],
 *    "tabs": [..], "actions": [..], "fields": [..] } ] }
 */
import { readFileSync } from 'node:fs'

const [oldPath = 'snapshot/sitemap.json', newPath = 'snapshot/sitemap.new.json'] = process.argv.slice(2)
const load = (p) => new Map(JSON.parse(readFileSync(p, 'utf8')).pages.map((pg) => [pg.id, pg]))
const before = load(oldPath)
const after = load(newPath)
const LISTS = ['tabs', 'actions', 'fields']
const report = []

for (const [id, pg] of after) {
  const old = before.get(id)
  if (!old) { report.push(`+ NEW PAGE ${pg.menuPath.join(' › ')}  (${pg.url})`); continue }
  const changes = []
  if (old.url !== pg.url) changes.push(`  url: ${old.url} → ${pg.url}`)
  if (old.menuPath.join('/') !== pg.menuPath.join('/')) changes.push(`  moved: ${old.menuPath.join(' › ')} → ${pg.menuPath.join(' › ')}`)
  for (const k of LISTS) {
    const a = new Set(old[k] ?? []), b = new Set(pg[k] ?? [])
    for (const x of b) if (!a.has(x)) changes.push(`  + ${k}: ${x}`)
    for (const x of a) if (!b.has(x)) changes.push(`  - ${k}: ${x}`)
  }
  if (changes.length) report.push(`~ ${pg.menuPath.join(' › ')}  → docs: ${(pg.docs ?? []).join(', ') || '(none)'}`, ...changes)
}
for (const [id, pg] of before) if (!after.has(id)) report.push(`- REMOVED ${pg.menuPath.join(' › ')}  → docs: ${(pg.docs ?? []).join(', ')}`)

console.log(report.length ? report.join('\n') : '✓ no differences')
