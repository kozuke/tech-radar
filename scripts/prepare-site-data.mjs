import { cp, mkdir, readdir, readFile, rm, writeFile } from 'node:fs/promises'
import { existsSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const dataDir = path.join(rootDir, 'data')
const dataItemsDir = path.join(dataDir, 'items')
const publicDataDir = path.join(rootDir, 'site', 'public', 'data')
const publicDataItemsDir = path.join(publicDataDir, 'items')
const siteArticlesDir = path.join(rootDir, 'site', 'articles')
const themeCssPath = path.join(rootDir, 'site', '.vitepress', 'theme', 'custom.css')
const designCssPath = path.join(rootDir, 'site', 'styles.css')
const slackSummaryPattern = /## 📢 Slack通知用サマリー\s*\n\s*<!-- SLACK_SUMMARY_START -->[\s\S]*?<!-- SLACK_SUMMARY_END -->\s*\n\s*---/m

function hideSlackSummarySection(content) {
  const hiddenSummaryBlock = (match) => {
    const [, summaryBlock = ''] = match.match(/(<!-- SLACK_SUMMARY_START -->[\s\S]*<!-- SLACK_SUMMARY_END -->)/m) || []

    if (!summaryBlock) {
      return match
    }

    return [
      '<div class="slack-summary-only" hidden aria-hidden="true">',
      '',
      summaryBlock.trim(),
      '',
      '</div>',
      '',
      '---'
    ].join('\n')
  }

  return content.replace(slackSummaryPattern, hiddenSummaryBlock)
}

// theme/custom.css は環境によって差し戻されるため、bolt 編集可能な site/styles.css を
// ビルド前に theme/custom.css へ上書きコピーする。これにより新デザインが必ず勝つ。
if (existsSync(designCssPath)) {
  const designCss = await readFile(designCssPath, 'utf8')
  await writeFile(themeCssPath, designCss, 'utf8')
  console.log('Applied site/styles.css -> theme/custom.css')
}

if (!existsSync(path.join(dataDir, 'index.json'))) {
  throw new Error('data/index.json was not found. Run the collector or add data before starting the site.')
}

await rm(publicDataDir, { recursive: true, force: true })
await mkdir(publicDataItemsDir, { recursive: true })
await cp(path.join(dataDir, 'index.json'), path.join(publicDataDir, 'index.json'))

if (existsSync(dataItemsDir)) {
  const itemFiles = await readdir(dataItemsDir)

  for (const file of itemFiles.filter((name) => name.endsWith('.meta.json'))) {
    await cp(path.join(dataItemsDir, file), path.join(publicDataItemsDir, file))
  }

  await mkdir(siteArticlesDir, { recursive: true })

  for (const file of await readdir(siteArticlesDir)) {
    if (/^\d{4}-\d{2}-\d{2}__daily-digest\.md$/.test(file)) {
      await rm(path.join(siteArticlesDir, file), { force: true })
    }
  }

  for (const file of itemFiles.filter((name) => name.endsWith('__daily-digest.md'))) {
    const src = path.join(dataItemsDir, file)
    const dest = path.join(siteArticlesDir, file)
    const raw = await readFile(src, 'utf8')
    const sanitized = hideSlackSummarySection(raw)
    if (sanitized.startsWith('---\nlastUpdated: false')) {
      await writeFile(dest, sanitized, 'utf8')
      continue
    }
    // Prepend `lastUpdated: false` frontmatter so VitePress skips the git-based
    // timestamp lookup (git may be unavailable in sandboxed dev environments).
    const withFrontmatter = sanitized.startsWith('---\n')
      ? sanitized.replace(/^---\n/, '---\nlastUpdated: false\n')
      : `---\nlastUpdated: false\n---\n\n${sanitized}`
    await writeFile(dest, withFrontmatter, 'utf8')
  }
}

console.log('Prepared site data from data/')
