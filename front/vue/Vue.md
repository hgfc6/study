Vue.js 是一套用于构建用户界面的渐进式 JavaScript 框架。它采用自底向上的增量开发设计，核心库专注于视图层，易于与其他库或已有项目整合。Vue.js 的目标是通过尽可能简单的 API 实现响应的数据绑定和组合的视图组件。

## 核心特点
* 响应式数据绑定：Vue.js 使用双向数据绑定，当数据变化时，视图会自动更新。
* 组件化：Vue.js 允许你将页面拆分为多个可复用的组件，每个组件都有自己的模板、逻辑和样式。
* 指令：Vue.js 提供了一系列内置指令（如 v-if, v-for, v-bind, v-on 等），用于简化 DOM 操作。
* 虚拟 DOM：Vue.js 使用虚拟 DOM 来提高渲染性能，只更新需要改变的部分。
* 单文件组件：Vue.js 支持单文件组件（.vue 文件），将模板、脚本和样式封装在一个文件中
 
## 高级特性
* Vuex：用于状态管理，适用于大型应用。
* Vue Router：用于构建单页面应用（SPA）的路由管理。
* Vue CLI：提供了一套完整的工具链，用于快速开发和构建 Vue.js 项目。
* Composition API：Vue 3 引入的新特性，提供了更灵活的逻辑复用方式。

## 适用场景
Vue.js 适用于构建中小型应用，也适用于大型复杂应用。由于其轻量级和易用性，Vue.js 被广泛应用于各种 Web 开发场景。

## 总结
Vue.js 是一个功能强大且易于上手的框架，适合各种规模的 Web 应用开发。通过其响应式数据绑定、组件化设计和丰富的生态系统，Vue.js 能够帮助开发者高效地构建现代化的 Web 应用。



<details class="lake-collapse"><summary id="u61745c28"><span class="ne-text">清单</span></summary><p id="u0648c5be" class="ne-p"><span class="ne-text" style="color: #DF2A3F; font-size: 19px">必学内容</span></p><ol class="ne-ol"><li id="u6aeac291" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">Vue.js 基础</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u0c12a618" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vue.js 简介</span></li><li id="u4246dea1" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vue 实例</span></li><li id="udf2c3914" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">模板语法</span></li><li id="ufc3eeb26" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">计算属性和侦听器</span></li><li id="uad10e715" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Class 与 Style 绑定</span></li><li id="u8dc8177f" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">条件渲染</span></li><li id="u4cf24f96" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">列表渲染</span></li><li id="u8a2671e4" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">事件处理</span></li><li id="u3f19baf4" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">表单输入绑定</span></li></ul></ul><ol start="2" class="ne-ol"><li id="u6b2ad9e9" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">组件</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u43851380" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">组件基础</span></li><li id="u5f54a620" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">组件注册</span></li><li id="u6c02b00c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Props</span></li><li id="u2f77f372" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">自定义事件</span></li><li id="u053f4ac1" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">插槽</span></li><li id="u9c365d3f" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">动态组件</span></li><li id="ud86bc21e" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">异步组件</span></li></ul></ul><ol start="3" class="ne-ol"><li id="u070277db" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">Vue Router</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="ue6c6a52e" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">路由基础</span></li><li id="u881c8896" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">嵌套路由</span></li><li id="u0cc76574" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">编程式导航</span></li><li id="ucb058ede" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">路由守卫</span></li><li id="ub0d8041c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">路由懒加载</span></li></ul></ul><ol start="4" class="ne-ol"><li id="ubbd11478" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">状态管理（Vuex）</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u50c2190d" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vuex 基础</span></li><li id="ua609fce5" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">State</span></li><li id="ucafb3b8c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Getters</span></li><li id="uc4c2df9f" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Mutations</span></li><li id="u78e83122" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Actions</span></li><li id="u310b5409" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Modules</span></li></ul></ul><ol start="5" class="ne-ol"><li id="ud9827857" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">Vue CLI</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="udb185608" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">项目创建</span></li><li id="u423915dd" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">项目结构</span></li><li id="u08f7774a" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">环境变量</span></li><li id="u9fa4b361" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">插件和配置</span></li></ul></ul><ol start="6" class="ne-ol"><li id="uf8ae54ab" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">生命周期钩子</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="uc8826534" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">创建阶段</span></li><li id="u56c28dce" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">挂载阶段</span></li><li id="ua7746a7c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">更新阶段</span></li><li id="u0b9cd1c4" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">销毁阶段</span></li></ul></ul><ol start="7" class="ne-ol"><li id="u5b17bbaa" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">API 请求</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="uf6b0fb2b" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Axios 基础</span></li><li id="u0a641c0e" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">请求拦截器</span></li><li id="u537dba0e" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">响应拦截器</span></li></ul></ul><p id="u82a753e8" class="ne-p"><strong><span class="ne-text" style="color: #DF2A3F; font-size: 19px">选学内容</span></strong></p><ol class="ne-ol"><li id="u45b9aff7" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">高级组件</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="uebfa12fb" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">渲染函数</span></li><li id="u406baf66" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">函数式组件</span></li><li id="u18f815d5" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">自定义指令</span></li><li id="u9d4ad651" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">过渡和动画</span></li></ul></ul><ol start="2" class="ne-ol"><li id="ua7b3ac45" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">Vuex 高级</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u84137d18" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vuex 插件</span></li><li id="u421ed43c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vuex 严格模式</span></li><li id="u39ee4a57" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vuex 测试</span></li></ul></ul><ol start="3" class="ne-ol"><li id="ud9a6918a" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">TypeScript 支持</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="ua54e8fa1" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vue 与 TypeScript 集成</span></li><li id="uc2d70e02" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">类型声明</span></li><li id="uaeb2ec97" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">类型推断</span></li></ul></ul><ol start="4" class="ne-ol"><li id="u8041d07a" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">服务端渲染（SSR）</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u1ac20a96" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Nuxt.js 基础</span></li><li id="u234b7111" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Nuxt.js 配置</span></li><li id="u3c820a04" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Nuxt.js 模块</span></li></ul></ul><ol start="5" class="ne-ol"><li id="u7aee5d69" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">测试</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u0f19567e" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">单元测试（Jest）</span></li><li id="uf4f8b464" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">端到端测试（Cypress）</span></li></ul></ul><ol start="6" class="ne-ol"><li id="uc55075fe" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">性能优化</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u73709024" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">懒加载</span></li><li id="uf4f890c1" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">代码分割</span></li><li id="ud02948ae" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">性能监控</span></li></ul></ul><ol start="7" class="ne-ol"><li id="u28f4ea06" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">PWA</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u2769a218" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">PWA 基础</span></li><li id="u39f7758c" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Service Worker</span></li><li id="u2f132b3f" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">离线缓存</span></li></ul></ul><ol start="8" class="ne-ol"><li id="u7286c27c" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">UI 框架</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u98f0e1c7" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Element UI</span></li><li id="udccca460" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vuetify</span></li><li id="udc34a6c8" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Ant Design Vue</span></li></ul></ul><ol start="9" class="ne-ol"><li id="u524c9aa3" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">国际化</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u032ff890" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">Vue I18n</span></li><li id="u85df62b4" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">多语言支持</span></li></ul></ul><ol start="10" class="ne-ol"><li id="ucbf76368" data-lake-index-type="0"><strong><span class="ne-text" style="font-size: 14px">安全性</span></strong></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u8b64049d" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">XSS 防护</span></li><li id="ua71fb841" data-lake-index-type="0"><span class="ne-text" style="font-size: 14px">CSRF 防护</span></li></ul></ul><p id="uc9b1a8ce" class="ne-p"><br></p></details>
Vue.js 是一个渐进式（小项目（核心库）>> 大项目（核心+插件）） JavaScript 框架，用于构建用户界面。以下是一个 Vue.js 的学习清单，涵盖了从基础到进阶的核心概念，并附上代码示例。

#### 1. **Vue.js 基础**
+ **安装与使用**
    - 使用 CDN 引入 Vue.js：

```html
<script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
```



    - 使用 Vue CLI 创建项目：

```bash
npm install -g @vue/cli
vue create my-project
```



+ **Vue 实例**

```javascript
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
});
```



+ **模板语法**

```html
<div id="app">
  <p>{{ message }}</p>
</div>
```



+ **指令**
  - `v-bind`：绑定属性

```html
<img v-bind:src="imageSrc">
```


  - `v-on`：绑定事件

```html
<button v-on:click="sayHello">Click me</button>
```



  - `v-model`：双向数据绑定

```html
<input v-model="message">
```



#### 2. **组件**
+ **组件定义**

```javascript
Vue.component('my-component', {
  template: '<div>A custom component!</div>'
});
```



+ **Props**

```javascript
Vue.component('child-component', {
  props: ['message'],
  template: '<div>{{ message }}</div>'
});
```



+ **组件通信**
    - 父组件向子组件传递数据：

```html
<child-component :message="parentMessage"></child-component>
```



    - 子组件向父组件发送事件：

```javascript
this.$emit('custom-event', data);
```



#### 3. **Vue Router**
+ **安装与配置**

```bash
npm install vue-router
```



```javascript
import Vue from 'vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter);

const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
];

const router = new VueRouter({
  routes
});

new Vue({
  router
}).$mount('#app');
```



+ **路由导航**

```html
<router-link to="/">Home</router-link>
<router-link to="/about">About</router-link>
```



#### 4. **Vuex**
+ **安装与配置**

```bash
npm install vuex
```



```javascript
import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  }
});

new Vue({
  store
}).$mount('#app');
```



+ **状态管理**

```javascript
this.$store.commit('increment');
```



#### 5. **高级特性**
+ **混入（Mixins）**

```javascript
const myMixin = {
  created() {
    this.hello();
  },
  methods: {
    hello() {
      console.log('Hello from mixin!');
    }
  }
};

new Vue({
  mixins: [myMixin]
});
```



+ **自定义指令**

```javascript
Vue.directive('focus', {
  inserted: function (el) {
    el.focus();
  }
});
```



+ **过渡与动画**

```html
<transition name="fade">
  <p v-if="show">Hello</p>
</transition>
```



#### 6. **测试**
+ **单元测试**

```bash
npm install --save-dev @vue/test-utils
```



```javascript
import { mount } from '@vue/test-utils';
import MyComponent from './MyComponent.vue';

test('renders a message', () => {
  const wrapper = mount(MyComponent, {
    propsData: {
      message: 'Hello'
    }
  });
  expect(wrapper.text()).toContain('Hello');
});
```



#### 7. **部署**
+ **构建生产版本**

```bash
npm run build
```



+ **部署到服务器** 将 `dist` 目录中的文件上传到服务器即可。

---

### 代码示例
#### 1. **基础示例**
```html
<div id="app">
  <p>{{ message }}</p>
  <input v-model="message">
</div>

<script>
  new Vue({
    el: '#app',
    data: {
      message: 'Hello Vue!'
    }
  });
</script>
```

CopyInsert

#### 2. **组件示例**
```html
<div id="app">
  <child-component :message="parentMessage"></child-component>
</div>

<script>
  Vue.component('child-component', {
    props: ['message'],
    template: '<div>{{ message }}</div>'
  });

  new Vue({
    el: '#app',
    data: {
      parentMessage: 'Hello from parent!'
    }
  });
</script>
```

CopyInsert

#### 3. **Vuex 示例**
```javascript
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  }
});

new Vue({
  el: '#app',
  store,
  methods: {
    increment() {
      this.$store.commit('increment');
    }
  }
});
```

CopyInsert

#### 4. **Vue Router 示例**
```javascript
const routes = [
  { path: '/', component: Home },
  { path: '/about', component: About }
];

const router = new VueRouter({
  routes
});

new Vue({
  router
}).$mount('#app');
```

