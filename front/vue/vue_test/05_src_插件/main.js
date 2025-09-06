import Vue from 'vue'
import App from './App.vue'
import plugins from "./plugins";

Vue.config.productionTip = false
Vue.use(plugins, 1, 2)//使用插件

new Vue({
    el: '#app',
    render: h => h(App)
})