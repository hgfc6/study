import Vue from 'vue'//实际是vue.runtime.esm.js内的Vue，是阉割版的，缺少模板解析器。所以不能使用template配置项。可以用render函数代替模板解析器
import App from './App.vue'

Vue.config.productionTip = false

const vm = new Vue({
  render: h => h(App),//实际是下面的这个render函数的简写，render函数是用来构建元素的，接受一个函数CreateElement函数作为参数
  // render(CreateElement) {
  //   return CreateElement(App)
  // },
  // template: `<h1>你好</h1>`,
  // components:{App}
}).$mount('#app')
