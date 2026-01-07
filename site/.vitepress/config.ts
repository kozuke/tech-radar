import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Tech Radar',
  description: '技術トレンドを自動収集・要約',
  lang: 'ja-JP',

  // GitHub Pages用のベースパス（リポジトリ名に合わせて変更）
  base: '/tech-radar/',

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/tech-radar/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#6366f1' }],
  ],

  themeConfig: {
    logo: '/logo.svg',

    nav: [
      { text: 'ホーム', link: '/' },
      { text: '記事一覧', link: '/articles/' },
      { text: 'タグ', link: '/tags/' },
      { text: 'About', link: '/about' },
    ],

    sidebar: {
      '/articles/': [
        {
          text: '記事',
          items: [
            { text: '最新記事', link: '/articles/' },
          ]
        }
      ]
    },

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
