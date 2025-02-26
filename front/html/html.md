以下是一份详细的 HTML 必学与选学清单，包含核心知识点和代码示例：

---

### **一、HTML 必学内容**
#### 1. 基础文档结构
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>页面标题</title>
</head>
<body>
    <!-- 页面内容 -->
</body>
</html>
```

#### 2. 常用标签
+ **标题与段落**：

```html
<h1>一级标题</h1>
<p>这是一个段落。</p>

```

+ **列表**：

```html
<!-- 无序列表 -->
<ul>
  <li>项目1</li>
  <li>项目2</li>
</ul>
<!-- 有序列表 -->
<ol>
  <li>第一步</li>
  <li>第二步</li>
</ol>

```

+ **链接与图片**：

```html
<a href="https://example.com" target="_blank">外部链接</a>
<img src="image.jpg" alt="图片描述" width="200">
```

+ **表格**：

```html
<table border="1">
  <tr>
    <th>姓名</th>
    <th>年龄</th>
  </tr>
  <tr>
    <td>张三</td>
    <td>25</td>
  </tr>
</table>

```

#### 3. 表单元素
```html
<form action="/submit" method="POST">
  <label for="username">用户名：</label>
  <input type="text" id="username" name="username" required>

  <label for="password">密码：</label>
  <input type="password" id="password" name="password">

  <input type="radio" id="male" name="gender" value="male">
  <label for="male">男</label>
  <input type="checkbox" id="subscribe" name="subscribe">
  <label for="subscribe">订阅新闻</label>
  <select name="city">
    <option value="bj">北京</option>
    <option value="sh">上海</option>
  </select>
  <textarea name="comment" rows="4" placeholder="请输入评论"></textarea>
  <button type="submit">提交</button>
</form>

```

#### 4. 语义化标签（HTML5）
```html
<header>页眉</header>
<nav>导航栏</nav>
<main>
  <article>
    <section>内容区块1</section>
    <section>内容区块2</section>
  </article>
  <aside>侧边栏</aside>
</main>
<footer>页脚</footer>

```

#### 5. 元数据与 SEO
```html
<head>
  <meta name="description" content="页面描述">
  <meta name="keywords" content="关键词1, 关键词2">
  <!-- 社交媒体优化 -->
  <meta property="og:title" content="分享标题">
</head>

```

---

### **二、HTML 选学内容**
#### 1. 多媒体嵌入
```html
<audio controls>
  <source src="audio.mp3" type="audio/mpeg">
</audio>
<video width="320" controls>
  <source src="video.mp4" type="video/mp4">
</video>
<!-- 嵌入 iframe -->
<iframe src="https://example.com" width="600" height="400"></iframe>

```

#### 2. Canvas 绘图
```html
<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
  const canvas = document.getElementById("myCanvas");
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "red";
  ctx.fillRect(10, 10, 50, 50);
</script>

```

#### 3. 高级表单功能
```html
<input type="color" name="favcolor">
<input type="date" name="birthday">
<input type="range" min="0" max="100">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
</datalist>
<input list="browsers" name="browser">
```

#### 4. Web Storage API（配合 JavaScript）
```html
<script>
  // 存储数据
  localStorage.setItem("username", "John");
  // 读取数据
  console.log(localStorage.getItem("username"));
</script>

```

#### 5. 响应式图片
```html
<picture>
  <source media="(min-width: 650px)" srcset="large.jpg">
  <source media="(min-width: 465px)" srcset="medium.jpg">
  <img src="small.jpg" alt="响应式图片">
</picture>

```

#### 6. Web Components（自定义元素）
```html
<!-- 定义自定义元素 -->
<script>
  class MyComponent extends HTMLElement {
    constructor() {
      super();
      this.innerHTML = "<h3>自定义组件</h3>";
    }
  }
  customElements.define("my-component", MyComponent);
</script>
<!-- 使用 -->
<my-component></my-component>

```