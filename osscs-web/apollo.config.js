// apollo.config.js
module.exports = {
    client: {
      service: {
        name: 'sandbox',
        // GraphQL API 的 URL
        url: 'http://127.0.0.1:8000/graphql/',
      },
      // 通过扩展名选择需要处理的文件
      includes: [
        'src/**/*.vue',
        'src/**/*.js',
      ],
    },
  }