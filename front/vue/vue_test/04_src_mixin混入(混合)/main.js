import Vue from 'vue'
import App from './App.vue'
import {mixin} from "./mixin";
import {mixin2} from "./mixin";

Vue.mixin(mixin)
Vue.mixin(mixin2)
new Vue({
    el:'#app',
    render: h => h(App)
})