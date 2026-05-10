import { cp, mkdir, readdir, rm } from 'node:fs/promises'
import { existsSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const rootDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const dataDir = path.join(rootDir, 'data')
const dataItemsDir = path.join(dataDir, 'items')
const publicDataDir = path.join(rootDir, 'site', 'public', 'data')
const publicDataItemsDir = path.join(publicDataDir, 'items')
const siteArticlesDir = path.join(rootDir, 'site', 'articles')

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
    await cp(path.join(dataItemsDir, file), path.join(siteArticlesDir, file))
  }
}

console.log('Prepared site data from data/')
