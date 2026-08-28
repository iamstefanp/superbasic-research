import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'SuperBasic™ Research',
  description: 'A program you run instead of improvising — research with every claim tied to a checkable source.',
  cleanUrls: true,

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
  ],

  themeConfig: {
    logo: '/favicon.svg',

    nav: [
      { text: 'Guide', link: '/guide/quick-start' },
      { text: 'Method', link: '/method/laws' },
      { text: 'Testing', link: '/testing/method-battery' },
      { text: 'Harness', link: '/harness/setup' },
      {
        text: 'GitHub',
        link: 'https://github.com/iamstefanp/superbasic-research',
      },
    ],

    sidebar: {
      '/guide/': [
        {
          text: 'Guide',
          items: [
            { text: 'Quick Start', link: '/guide/quick-start' },
            { text: 'Connect Your Setup', link: '/guide/connect' },
            { text: 'Security & Legal', link: '/guide/security-legal' },
          ],
        },
      ],
      '/method/': [
        {
          text: 'The Method',
          items: [
            { text: 'The Laws', link: '/method/laws' },
            { text: 'The Eight Phases', link: '/method/phases' },
            { text: 'Modes & Confidence', link: '/method/modes-confidence' },
            { text: 'Standards', link: '/method/standards' },
          ],
        },
      ],
      '/testing/': [
        {
          text: 'Testing',
          items: [
            { text: 'Method Battery', link: '/testing/method-battery' },
            { text: 'Red-Team Evaluation', link: '/testing/red-team' },
            { text: 'Cross-Model Log', link: '/testing/cross-model' },
          ],
        },
      ],
      '/harness/': [
        {
          text: 'The Harness',
          items: [
            { text: 'Setup & Backends', link: '/harness/setup' },
            { text: 'Maintenance', link: '/harness/maintenance' },
          ],
        },
      ],
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/iamstefanp/superbasic-research' },
    ],

    footer: {
      message: 'CC BY-SA 4.0 — the method is open, the name is not. See TRADEMARK.md.',
      copyright: 'Built by Stefan Petcov / Runway Services',
    },

    search: {
      provider: 'local',
    },

    editLink: {
      pattern: 'https://github.com/iamstefanp/superbasic-research/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },
  },
})
