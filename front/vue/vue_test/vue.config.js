const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, /*关闭语法检查*/
  pages: {// https://cli.vuejs.org/zh/config/#pages
    index: {
      // 入口
      entry: 'src/main.js'
    }
  }
})
