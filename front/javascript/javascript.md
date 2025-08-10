## **一、必学核心知识**（掌握后能应对大部分开发需求）
### **1. JavaScript 基础**
+ **语法基础**：变量、数据类型、运算符、流程控制（`if/else`、`for`、`while`）、[函数定义](./function_define.js)。
+ **核心概念**：
    - 作用域（全局/函数/块级作用域）、[闭包](./js_basic.js)（Closure）。
    - [this](./this.html) 的指向规则、`call/apply/bind`。
    - [原型链](./prototype_chain.html)（Prototype Chain）、[继承](./es5_es6_extends.html)（ES5 和 ES6 的 `class`）。
    - [异步编程](./async.html)：回调函数、`Promise`、`async/await`。
    - [模块化](./module/module.md)：`CommonJS`（Node.js）、`ES Modules`（浏览器）。
+ **[内置对象](./js_basic.js)**：`Array`、`Object`、`String`、`Date`、`Math`、`JSON`、`Map/Set`。

### **2. Web API**
+ **[DOM 操作](./webapi/DOM.html)**：节点增删改查、事件监听（`addEventListener`）、事件冒泡与捕获。
+ **[BOM 对象](./webapi/BOM.html)**：`window`、`location`、`history`、`navigator`。
+ **[网络请求](./webapi/internet.html)**：`XMLHttpRequest`、`Fetch API`、`WebSocket`。
+ **[浏览器存储](./browser_storage.js)**：`Cookie`、`LocalStorage`、`SessionStorage`、`IndexedDB`（基础用法）。

### **3. 工具链**
+ **包管理**：`npm`/`yarn`/`pnpm`（安装、依赖管理、脚本命令）。
+ **构建工具**：`Webpack`/`Vite`（基础配置、打包优化）。
+ **代码规范**：`ESLint`、`Prettier`。
+ **调试工具**：浏览器开发者工具（Console、Sources、Network）、`debugger` 语句。

### **4. 现代框架（至少精通一个）**
+ **React**：JSX、组件化、Hooks（`useState`、`useEffect`）、状态管理（Context API）。
+ **Vue**：模板语法、响应式原理、组合式 API（`ref`、`reactive`）、Vue Router、Pinia。
+ **Angular**：TypeScript 集成、依赖注入、RxJS、NgModules。

---

## **二、选学进阶方向**（根据职业方向选择）
### **1. 前端工程化**
+ **构建工具进阶**：Webpack 插件开发、Vite 原理、Tree Shaking、代码分割。
+ **模块联邦**：微前端架构（`Module Federation`）。
+ **性能优化**：Lighthouse 分析、CDN 加速、缓存策略、SSR/SSG（Next.js/Nuxt.js）。

### **2. 后端与全栈**
+ **Node.js**：核心模块（`fs`、`path`、`http`）、Express/Koa 框架、RESTful API 设计。
+ **数据库**：MongoDB（NoSQL）、PostgreSQL（SQL）、ORM（Mongoose、Prisma）。
+ **身份认证**：JWT、OAuth2.0、Session/Cookie 安全。
+ **部署与运维**：Docker 基础、Nginx 配置、CI/CD（GitHub Actions）。

### **3. 高级前端**
+ **TypeScript**：类型系统、泛型、装饰器、工程化集成。
+ **状态管理**：Redux（中间件、Redux Toolkit）、Vuex、MobX。
+ **测试工具**：单元测试（Jest）、E2E 测试（Cypress、Playwright）。
+ **数据可视化**：D3.js、ECharts、Canvas/SVG 渲染。

### **4. 新兴技术**
+ **WebAssembly**：用 C/C++/Rust 编写高性能模块。
+ **PWA**：Service Worker、离线缓存、推送通知。
+ **Web Components**：自定义元素、Shadow DOM。
+ **WebGL/Three.js**：3D 可视化与游戏开发。

---

## **三、学习资源推荐**
+ **书籍**：
    - 《JavaScript 高级程序设计》（红宝书）。
    - 《你不知道的 JavaScript》系列（深入理解核心机制）。
    - 《深入浅出 Node.js》（朴灵）。
+ **文档**：
    - [MDN Web Docs](https://developer.mozilla.org/)（最权威的 Web 技术文档）。
    - [ES6 入门教程](https://es6.ruanyifeng.com/)（阮一峰）。
+ **实战平台**：
    - LeetCode（算法练习）。
    - CodeSandbox/StackBlitz（在线编码）。
    - 个人项目（从 TodoList 到完整应用）。

---

## **四、学习建议**
1. **优先掌握必学部分**，再根据兴趣或岗位需求扩展选学方向。
2. **动手实践**：通过项目驱动学习（如搭建博客、电商后台、数据看板）。
3. **阅读源码**：学习主流库（如 Lodash、Axios）和框架（React/Vue）的实现。
4. **参与社区**：关注 GitHub 趋势项目、参加技术会议（如 VueConf、JSConf）。

---

掌握这些内容后，你将能胜任从初级到高级的前端/全栈开发工作，并根据技术趋势持续迭代知识体系！ 🚀



---

---

以下是在原答案基础上补充的 **代码示例清单**，帮助理解关键知识点：

---

## **一、必学核心知识代码示例**
### **1. JavaScript 基础**
#### **闭包（Closure）**
```javascript
function createCounter() {
  let count = 0;
  return function() {
    count++;
    console.log(count);
  };
}

const counter = createCounter();
counter(); // 1
counter(); // 2 （闭包保留了 count 的状态）
```

#### **原型链（Prototype Chain）**
```javascript
function Animal(name) {
  this.name = name;
}

// 在原型上添加方法
Animal.prototype.speak = function() {
  console.log(`${this.name} makes a noise`);
};

class Dog extends Animal {
  speak() {
    console.log(`${this.name} barks`);
  }
}

const dog = new Dog('Buddy');
dog.speak(); // "Buddy barks" （通过原型链继承并覆盖方法）
```

#### **Promise 与 async/await**
```javascript
// Promise 链式调用
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));

// async/await 写法
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}
```

---

### **2. Web API**
#### **DOM 操作与事件**
```html
<button id="myButton">Click me</button>
<script>
  const button = document.getElementById('myButton');
  button.addEventListener('click', () => {
    button.textContent = 'Clicked!';
  });
</script>

```

#### **Fetch API**
```javascript
// 发起 GET 请求
fetch('https://api.example.com/users')
  .then(response => response.json())
  .then(users => {
    users.forEach(user => {
      console.log(user.name);
    });
  });
```

#### **LocalStorage 使用**
```javascript
// 存储数据
localStorage.setItem('theme', 'dark');

// 读取数据
const theme = localStorage.getItem('theme');
console.log(theme); // 'dark'
```

---

### **3. 工具链**
#### **npm 脚本（package.json）**
```json
{
  "scripts": {
    "start": "webpack serve --mode development",
    "build": "webpack --mode production",
    "lint": "eslint src/**/*.js2"
  }
}
```

#### **Webpack 基础配置（webpack.config.js）**
```javascript
module.exports = {
  entry: './src/index.js2',
  output: {
    filename: 'bundle.js2',
    path: path.resolve(__dirname, 'dist'),
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
    ],
  },
};
```

---

### **4. 现代框架**
#### **React Hooks**
```jsx
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

#### **Vue 响应式数据**
```vue
<template>
  <div>
    <p>{{ message }}</p>
    <button @click="reverseMessage">Reverse</button>
  </div>
</template>
<script setup>
import { ref } from 'vue';

const message = ref('Hello Vue!');

function reverseMessage() {
  message.value = message.value.split('').reverse().join('');
}
</script>

```

#### **Angular 组件**
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h1>{{ title }}</h1>
    <button (click)="onClick()">Click me</button>
  `,
})
export class AppComponent {
  title = 'My Angular App';

  onClick() {
    console.log('Button clicked!');
  }
}
```

---

## **二、选学进阶方向代码示例**
### **1. 前端工程化**
#### **Webpack 插件示例**
```javascript
// 自定义 Webpack 插件（生成版权注释）
class CopyrightPlugin {
  apply(compiler) {
    compiler.hooks.emit.tap('CopyrightPlugin', (compilation) => {
      compilation.assets['copyright.txt'] = {
        source: () => 'Copyright 2023 by Me',
        size: () => 20,
      };
    });
  }
}

// 在配置中使用插件
module.exports = {
  plugins: [new CopyrightPlugin()],
};
```

---

### **2. 后端与全栈**
#### **Express 路由**
```javascript
const express = require('express');
const app = express();

app.get('/api/users', (req, res) => {
  res.json([{ id: 1, name: 'Alice' }, { id: 2, name: 'Bob' }]);
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

---

### **3. 高级前端**
#### **TypeScript 类型注解**
```typescript
interface User {
  id: number;
  name: string;
}

function getUser(id: number): User {
  return { id: 1, name: 'Alice' };
}

const user: User = getUser(1);
console.log(user.name); // 'Alice'
```

#### **Jest 单元测试**
```javascript
// sum.js2
function sum(a, b) {
  return a + b;
}

// sum.test.js2
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

#### **ECharts 数据可视化**
```html
<div id="chart" style="width: 600px; height: 400px;"></div>
<script>
  const chart = echarts.init(document.getElementById('chart'));
  chart.setOption({
    xAxis: { data: ['A', 'B', 'C'] },
    yAxis: {},
    series: [{ type: 'bar', data: [10, 20, 30] }],
  });
</script>

```

---

### **4. 新兴技术**
#### **Web Components**
```html
<custom-button label="Click me"></custom-button>
<script>
  class CustomButton extends HTMLElement {
    constructor() {
      super();
      const shadow = this.attachShadow({ mode: 'open' });
      const button = document.createElement('button');
      button.textContent = this.getAttribute('label');
      shadow.appendChild(button);
    }
  }

  customElements.define('custom-button', CustomButton);
</script>

```
