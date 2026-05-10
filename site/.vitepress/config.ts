import { defineConfig } from 'vitepress'

const siteBase = process.env.VITEPRESS_BASE ?? (process.env.npm_lifecycle_event === 'dev' ? '/' : '/tech-radar/')

export default defineConfig({
  title: 'Tech Radar',
  description: '技術トレンドを自動収集・要約',
  lang: 'ja-JP',

  // dev previews use root for tools like Bolt; production builds keep the GitHub Pages repo path.
  base: siteBase,

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: `${siteBase}logo.svg` }],
    ['meta', { name: 'theme-color', content: '#0f766e' }],
  ],

  themeConfig: {
    logo: '/logo.svg',

    nav: [
      { text: 'ホーム', link: '/' },
      { text: 'タグ', link: '/tags/' },
      { text: 'About', link: '/about' },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/your-username/tech-radar' }
    ],

    footer: {
      message: 'Powered by VitePress & OpenRouter AI',
      copyright: '© 2026 Tech Radar'
    },

    search: {
      provider: 'local',
      options: {
        translations: {
          button: {
            buttonText: '検索',
            buttonAriaLabel: '検索'
          },
          modal: {
            noResultsText: '結果が見つかりません',
            resetButtonTitle: 'リセット',
            footer: {
              selectText: '選択',
              navigateText: '移動',
              closeText: '閉じる'
            }
          }
        }
      }
    },

    outline: {
      label: '目次',
      level: [2, 3]
    },

    docFooter: {
      prev: '前の記事',
      next: '次の記事'
    },

    lastUpdated: {
      text: '最終更新',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'short'
      }
    }
  },

  vite: {
    // data/からJSONを読み込めるように設定
    server: {
      fs: {
        allow: ['..']
      }
    }
  }
})
