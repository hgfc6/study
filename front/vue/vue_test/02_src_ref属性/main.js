import Vue from 'vue'//引入Vue
import App from './App.vue'//引入App
Vue.config.productionTip = false//关闭vue生产提示

//创建vm
new Vue({
    el: '#app',
    render: h => h(App)
})