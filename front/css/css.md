## 一、必学核心知识（构建网页基础）
### **1. 选择器与优先级**
#### **基础选择器**
```css
/* 标签选择器 */
p { color: #333; }

/* 类选择器 */
.button { padding: 8px 16px; }

/* ID 选择器（慎用，优先级过高） */
#header { background: #fff; }

/* 通配符选择器 */
* { margin: 0; padding: 0; }
```

#### **组合选择器**
```css
/* 后代选择器 */
nav ul li { display: inline-block; }

/* 子代选择器 */
.parent > .child { border: 1px solid #ccc; }

/* 相邻兄弟选择器 */
h2 + p { margin-top: 10px; }

/* 并集选择器 */
h1, h2, h3 { font-family: Arial; }
```

#### **伪类与伪元素**
```css
/* 链接状态 */
a:hover { color: red; }
a:active { color: blue; }

/* 表单元素 */
input:focus { outline: 2px solid #4CAF50; }

/* 首行与首字母 */
p::first-line { font-weight: bold; }
p::first-letter { font-size: 2em; }
```

#### **优先级计算**
```css
/* 优先级权重：行内样式(1000) > ID(100) > 类/伪类(10) > 标签(1) */
#nav .item.active { color: red; } /* 权重：100 + 10 + 10 = 120 */
```

---

### **2. 盒模型与布局**
#### **盒模型组成**
```css
.box {
  width: 200px;          /* 内容宽度 */
  padding: 20px;         /* 内边距 */
  border: 2px solid #000;/* 边框 */
  margin: 10px;          /* 外边距 */
  box-sizing: border-box;/* 切换为 border-box 模型（总宽度=width） */
}
```

#### **居中布局**
```css
/* Flex 水平垂直居中 */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 300px;
}

/* Grid 居中 */
.container {
  display: grid;
  place-items: center;
}

/* 绝对定位居中 */
.parent {
  position: relative;
}
.child {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
```

---

### **3. 布局技术**
#### **Flex 弹性布局**
```css
.container {
  display: flex;
  gap: 10px;            /* 子项间距 */
  flex-wrap: wrap;       /* 允许换行 */
}
.item {
  flex: 1;              /* 自适应填充 */
  min-width: 200px;     /* 最小宽度 */
}
```

<details class="lake-collapse"><summary id="ud11e132e"><span class="ne-text">详解</span></summary><p id="u4bf3809e" class="ne-p"><span class="ne-text">CSS中的Flex（弹性布局）是一种一维布局模型，主要针对容器中的子元素进行排布和对齐。Flex布局的优势在于它可以自动调整子元素的大小和顺序，以适应不同的屏幕尺寸和设备。</span></p><h3 id="e2d6d0e3"><span class="ne-text">基本概念</span></h3><ul class="ne-ul"><li id="u50ad48cd" data-lake-index-type="0"><strong><span class="ne-text">容器（Flex container）</span></strong><span class="ne-text">：应用了</span><code class="ne-code"><span class="ne-text">display: flex;</span></code><span class="ne-text">或</span><code class="ne-code"><span class="ne-text">display: inline-flex;</span></code><span class="ne-text">的元素。其子元素将按照弹性布局规则进行排列。</span></li><li id="uf97e2bc7" data-lake-index-type="0"><strong><span class="ne-text">项目（Flex items）</span></strong><span class="ne-text">：容器中的直接子元素，按照弹性布局规则进行对齐和调整大小。</span></li></ul><h3 id="d6ed1fc8"><span class="ne-text">常用Flex属性</span></h3><h4 id="07788d44"><span class="ne-text">容器属性</span></h4><ul class="ne-ul"><li id="u3d9fa69c" data-lake-index-type="0"><strong><span class="ne-text">display</span></strong><span class="ne-text">：定义一个flex容器。</span><code class="ne-code"><span class="ne-text">display: flex;</span></code><span class="ne-text"> 创建一个块级的弹性布局容器，</span><code class="ne-code"><span class="ne-text">display: inline-flex;</span></code><span class="ne-text"> 创建一个内联的弹性布局容器。</span></li><li id="u24a93b55" data-lake-index-type="0"><strong><span class="ne-text">flex-direction</span></strong><span class="ne-text">：定义主轴的方向。可选值有</span><code class="ne-code"><span class="ne-text">row</span></code><span class="ne-text">（默认，从左到右），</span><code class="ne-code"><span class="ne-text">row-reverse</span></code><span class="ne-text">（从右到左），</span><code class="ne-code"><span class="ne-text">column</span></code><span class="ne-text">（从上到下），</span><code class="ne-code"><span class="ne-text">column-reverse</span></code><span class="ne-text">（从下到上）。</span></li><li id="u6b63ef78" data-lake-index-type="0"><strong><span class="ne-text">justify-content</span></strong><span class="ne-text">：定义主轴上的对齐方式。可选值包括</span><code class="ne-code"><span class="ne-text">flex-start</span></code><span class="ne-text">（默认，项目向起始位置对齐），</span><code class="ne-code"><span class="ne-text">flex-end</span></code><span class="ne-text">（项目向结束位置对齐），</span><code class="ne-code"><span class="ne-text">center</span></code><span class="ne-text">（项目居中对齐），</span><code class="ne-code"><span class="ne-text">space-between</span></code><span class="ne-text">（项目两端对齐，间隔相等），</span><code class="ne-code"><span class="ne-text">space-around</span></code><span class="ne-text">（每个项目两侧间隔相等）。</span></li><li id="u610eaec2" data-lake-index-type="0"><strong><span class="ne-text">align-items</span></strong><span class="ne-text">：定义交叉轴上的对齐方式。可选值包括</span><code class="ne-code"><span class="ne-text">stretch</span></code><span class="ne-text">（默认，项目被拉伸以适应容器），</span><code class="ne-code"><span class="ne-text">flex-start</span></code><span class="ne-text">（交叉轴的起始位置对齐），</span><code class="ne-code"><span class="ne-text">flex-end</span></code><span class="ne-text">（交叉轴的结束位置对齐），</span><code class="ne-code"><span class="ne-text">center</span></code><span class="ne-text">（交叉轴的居中对齐），</span><code class="ne-code"><span class="ne-text">baseline</span></code><span class="ne-text">（项目的第一行文字的基线对齐）。</span></li><li id="uaf602dea" data-lake-index-type="0"><strong><span class="ne-text">align-content</span></strong><span class="ne-text">：定义多根轴线的对齐方式。只在容器有多根轴线（即子元素换行）时才有作用。可选值包括</span><code class="ne-code"><span class="ne-text">stretch</span></code><span class="ne-text">（默认，轴线被拉伸以适应容器），</span><code class="ne-code"><span class="ne-text">flex-start</span></code><span class="ne-text">（交叉轴的起始位置对齐），</span><code class="ne-code"><span class="ne-text">flex-end</span></code><span class="ne-text">（交叉轴的结束位置对齐），</span><code class="ne-code"><span class="ne-text">center</span></code><span class="ne-text">（交叉轴的居中对齐），</span><code class="ne-code"><span class="ne-text">space-between</span></code><span class="ne-text">（轴线之间的间隔相等），</span><code class="ne-code"><span class="ne-text">space-around</span></code><span class="ne-text">（轴线两侧的间隔相等）。</span></li></ul><h4 id="86de2a91"><span class="ne-text">项目属性</span></h4><ul class="ne-ul"><li id="uc0132b94" data-lake-index-type="0"><strong><span class="ne-text">order</span></strong><span class="ne-text">：定义项目的排列顺序，数值越小越靠前，默认为</span><code class="ne-code"><span class="ne-text">0</span></code><span class="ne-text">。</span></li><li id="u94e2e157" data-lake-index-type="0"><strong><span class="ne-text">flex-grow</span></strong><span class="ne-text">：定义项目的放大比例，默认为</span><code class="ne-code"><span class="ne-text">0</span></code><span class="ne-text">。如果所有项目的</span><code class="ne-code"><span class="ne-text">flex-grow</span></code><span class="ne-text">属性都为</span><code class="ne-code"><span class="ne-text">1</span></code><span class="ne-text">，则它们将等分剩余空间。如果一个项目的</span><code class="ne-code"><span class="ne-text">flex-grow</span></code><span class="ne-text">属性为</span><code class="ne-code"><span class="ne-text">2</span></code><span class="ne-text">，其他项目为</span><code class="ne-code"><span class="ne-text">1</span></code><span class="ne-text">，则前者占据的剩余空间将比后者多一倍。</span></li><li id="ub01fed50" data-lake-index-type="0"><strong><span class="ne-text">flex-shrink</span></strong><span class="ne-text">：定义项目的缩小比例，默认为</span><code class="ne-code"><span class="ne-text">1</span></code><span class="ne-text">，即项目将缩小。它接受一个无单位的值作为比例，数值越大，项目缩小越多。</span></li><li id="uab43e41f" data-lake-index-type="0"><strong><span class="ne-text">flex-basis</span></strong><span class="ne-text">：定义在分配多余空间之前，项目占据的主轴空间。浏览器根据这个属性，计算主轴是否有多余空间。它的默认值为</span><code class="ne-code"><span class="ne-text">auto</span></code><span class="ne-text">，即项目的本来大小。</span></li><li id="ub22e2343" data-lake-index-type="0"><strong><span class="ne-text">flex</span></strong><span class="ne-text">：是</span><code class="ne-code"><span class="ne-text">flex-grow</span></code><span class="ne-text">,</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">flex-shrink</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">flex-basis</span></code><span class="ne-text">的简写，默认为</span><code class="ne-code"><span class="ne-text">0 1 auto</span></code><span class="ne-text">。</span></li><li id="u833956c2" data-lake-index-type="0"><strong><span class="ne-text">align-self</span></strong><span class="ne-text">：允许单个项目有与其他项目不一样的对齐方式，可覆盖</span><code class="ne-code"><span class="ne-text">align-items</span></code><span class="ne-text">属性。默认值为</span><code class="ne-code"><span class="ne-text">auto</span></code><span class="ne-text">，即继承父元素的</span><code class="ne-code"><span class="ne-text">align-items</span></code><span class="ne-text">属性，如果没有父元素，则等同于</span><code class="ne-code"><span class="ne-text">stretch</span></code><span class="ne-text">。</span></li></ul><h3 id="1a63ac23"><span class="ne-text">示例</span></h3><pre data-language="css" id="Gfj4j" class="ne-codeblock language-css"><code>.container {
    display: flex;
    flex-direction: row; /* 或 column */
    justify-content: center; /* 或 space-between, space-around, flex-start, flex-end */
    align-items: center; /* 或 flex-start, flex-end, stretch, baseline */
    align-content: stretch; /* 或 flex-start, flex-end, center, space-between, space-around (仅当 flex-wrap 设置为 wrap 或 wrap-reverse 时有效) */
}

.item {
order: 2; /* 项目默认按源代码顺序排列，order 为 2 时该项目排在后 */
flex-grow: 1; /* 项目放大比例为 1 */
flex-shrink: 1; /* 项目缩小比例为 1 */
flex-basis: auto; /* 项目占据空间为默认大小 */
flex: 1 1 auto; /* 简写形式 */
align-self: flex-start; /* 该项目交叉轴方向上的对齐方式 */
}</code></pre><p id="u981852b2" class="ne-p" style="text-align: right"><span class="ne-text">Copy</span><span class="ne-text">Insert</span></p><h3 id="7efcb0ce"><span class="ne-text">使用场景</span></h3><p id="ue52906b4" class="ne-p"><span class="ne-text">Flex布局特别适用于需要自动调整大小和位置的布局需求，比如响应式设计、导航栏、列表等。通过设置</span><code class="ne-code"><span class="ne-text">flex-direction</span></code><span class="ne-text">和</span><code class="ne-code"><span class="ne-text">justify-content</span></code><span class="ne-text">，可以轻松地实现复杂的布局效果，无需使用浮动（float）或定位（position）等传统布局方法。</span></p><p id="uf0b4afe1" class="ne-p"><br></p></details>
#### **Grid 网格布局**
```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 三列等宽 */
  grid-template-rows: 100px auto;
  gap: 20px;
}
.item-1 {
  grid-column: 1 / 3;   /* 占据第1到第2列 */
  grid-row: 1;
}
```

<details class="lake-collapse"><summary id="u7f5d3657"><span class="ne-text" style="font-size: 16px">详解</span></summary><p id="u3b58c3c4" class="ne-p"><br></p><p id="u5d5f1c98" class="ne-p"><span class="ne-text">Grid布局是一种二维布局系统，可以同时控制行和列，非常适合用于复杂的页面布局。使用Grid布局时，首先需要定义一个网格容器，通过设置</span><code class="ne-code"><span class="ne-text">display: grid;</span></code><span class="ne-text">或</span><code class="ne-code"><span class="ne-text">display: inline-grid;</span></code><span class="ne-text">来实现。</span></p><h3 id="262b54aa"><span class="ne-text">Grid布局的基本概念</span></h3><ul class="ne-ul"><li id="u6a20d905" data-lake-index-type="0"><strong><span class="ne-text">网格容器（Grid Container）</span></strong><span class="ne-text">：使用</span><code class="ne-code"><span class="ne-text">display: grid;</span></code><span class="ne-text">或</span><code class="ne-code"><span class="ne-text">display: inline-grid;</span></code><span class="ne-text">创建的元素。</span></li><li id="ueb533105" data-lake-index-type="0"><strong><span class="ne-text">网格项目（Grid Item）</span></strong><span class="ne-text">：在网格容器内直接子元素，自动成为网格项。</span></li><li id="ueca2c265" data-lake-index-type="0"><strong><span class="ne-text">行（Row）</span></strong><strong><span class="ne-text">和</span></strong><strong><span class="ne-text">列（Column）</span></strong><span class="ne-text">：网格由多个行和列组成，可以通过设置行和列的大小来控制布局。</span></li><li id="u6da14003" data-lake-index-type="0"><strong><span class="ne-text">网格线（Grid Line）</span></strong><span class="ne-text">：将网格项目分隔的线，可以通过线的位置来控制项目的排放。</span></li></ul><p id="uf3310ff4" class="ne-p"><span class="ne-text">以下是一些Grid布局的关键属性：</span></p><ol class="ne-ol"><li id="u29b9e64a" data-lake-index-type="0"><strong><span class="ne-text">定义网格容器</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u25341532" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">display: grid;</span></code><span class="ne-text">：将元素设置为网格容器。</span></li><li id="ufaa30e05" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">display: inline-grid;</span></code><span class="ne-text">：将元素设置为内联网格容器。</span></li></ul></ul><ol start="2" class="ne-ol"><li id="u6c97fb4f" data-lake-index-type="0"><strong><span class="ne-text">定义网格模板</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u7627f193" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-template-columns</span></code><span class="ne-text">：定义网格列的宽度。例如，</span><code class="ne-code"><span class="ne-text">grid-template-columns: 100px 100px 100px;</span></code><span class="ne-text">将创建三列，每列宽度为100px。</span></li><li id="u84ecc1be" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-template-rows</span></code><span class="ne-text">：定义网格行的高度。例如，</span><code class="ne-code"><span class="ne-text">grid-template-rows: 50px 50px;</span></code><span class="ne-text">将创建两行，每行高度为50px。</span></li><li id="u734ca248" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-template-areas</span></code><span class="ne-text">：通过命名区域来定义网格布局。例如，</span><code class="ne-code"><span class="ne-text">grid-template-areas: &quot;header header&quot; &quot;nav content&quot; &quot;footer footer&quot;;</span></code><span class="ne-text">定义了三个区域：header、nav、content和footer。</span></li></ul></ul><ol start="3" class="ne-ol"><li id="u7c489fd5" data-lake-index-type="0"><strong><span class="ne-text">自动调整网格</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="ud633d57d" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-auto-columns</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">grid-auto-rows</span></code><span class="ne-text">：定义未明确指定大小的网格项的默认大小。</span></li><li id="uf59997f9" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-auto-flow</span></code><span class="ne-text">：定义自动放置网格项的算法，可以设置为</span><code class="ne-code"><span class="ne-text">row</span></code><span class="ne-text">（默认）、</span><code class="ne-code"><span class="ne-text">column</span></code><span class="ne-text">或</span><code class="ne-code"><span class="ne-text">row dense</span></code><span class="ne-text">、</span><code class="ne-code"><span class="ne-text">column dense</span></code><span class="ne-text">。</span></li></ul></ul><ol start="4" class="ne-ol"><li id="u41992825" data-lake-index-type="0"><strong><span class="ne-text">间隙</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="uf1243b9e" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-column-gap</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">grid-row-gap</span></code><span class="ne-text">：定义列与列、行与行之间的间隙。</span></li><li id="u36b83fb0" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">gap</span></code><span class="ne-text">：同时设置网格行和列的间隙，简化了写法。</span></li></ul></ul><ol start="5" class="ne-ol"><li id="ub5155e89" data-lake-index-type="0"><strong><span class="ne-text">对齐内容</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u8d8561d5" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">justify-items</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">align-items</span></code><span class="ne-text">：用于定义网格容器中所有网格项在各自网格区域内的水平和垂直对齐方式。</span></li><li id="u29f96979" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">justify-content</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">align-content</span></code><span class="ne-text">：用于定义整个网格在网格容器内的水平和垂直对齐方式。</span></li></ul></ul><ol start="6" class="ne-ol"><li id="u60b581d0" data-lake-index-type="0"><strong><span class="ne-text">放置网格项</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u9c4f0a74" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-column</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">grid-row</span></code><span class="ne-text">：定义网格项占据的列和行。</span></li><li id="ua3a81fe0" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-area</span></code><span class="ne-text">：可以同时指定网格项占据的行和列，或者通过命名区域来放置。</span></li></ul></ul><ol start="7" class="ne-ol"><li id="u055373e5" data-lake-index-type="0"><strong><span class="ne-text">命名线</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="u161cbda8" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">grid-column-start</span></code><span class="ne-text">、</span><code class="ne-code"><span class="ne-text">grid-column-end</span></code><span class="ne-text">、</span><code class="ne-code"><span class="ne-text">grid-row-start</span></code><span class="ne-text"> </span><span class="ne-text">和</span><span class="ne-text"> </span><code class="ne-code"><span class="ne-text">grid-row-end</span></code><span class="ne-text">：允许你通过命名行来更精确地控制网格项的位置。</span></li></ul></ul><ol start="8" class="ne-ol"><li id="u0d9829fc" data-lake-index-type="0"><strong><span class="ne-text">重复模式</span></strong><span class="ne-text">：</span></li></ol><ul class="ne-list-wrap"><ul ne-level="1" class="ne-ul"><li id="uc452e335" data-lake-index-type="0"><code class="ne-code"><span class="ne-text">repeat()</span></code><span class="ne-text">：可以用于简化重复的列或行定义。例如，</span><code class="ne-code"><span class="ne-text">grid-template-columns: repeat(3, 100px);</span></code><span class="ne-text">创建了三列，每列宽度为100px。</span></li></ul></ul><p id="u611ee388" class="ne-p"><span class="ne-text">通过结合这些属性，你可以创建出非常复杂的布局结构，满足各种设计需求。Grid布局的灵活性和强大的功能使其成为现代Web设计中不可或缺的一部分。</span></p><p id="u42f35b59" class="ne-p"><span class="ne-text">以下是一个代码示例</span></p><pre data-language="css" id="CYeyg" class="ne-codeblock language-css"><code>&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;zh&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;CSS Grid布局示例&lt;/title&gt;
    &lt;style&gt;
        .grid-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr); /* 三列均分 */
            grid-template-rows: 100px 200px; /* 两行，第一行100px，第二行200px */
            gap: 10px; /* 项目间距 */
        }
        .item1 { background-color: lightblue; }
        .item2 { background-color: lightgreen; }
        .item3 { background-color: lightcoral; }
        .item4 { background-color: lightyellow; }
        .item5 { background-color: lightpink; }
        .item6 { background-color: lightgray; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;div class=&quot;grid-container&quot;&gt;
&lt;div class=&quot;item1&quot;&gt;项目 1&lt;/div&gt;
&lt;div class=&quot;item2&quot;&gt;项目 2&lt;/div&gt;
&lt;div class=&quot;item3&quot;&gt;项目 3&lt;/div&gt;
&lt;div class=&quot;item4&quot;&gt;项目 4&lt;/div&gt;
&lt;div class=&quot;item5&quot;&gt;项目 5&lt;/div&gt;
&lt;div class=&quot;item6&quot;&gt;项目 6&lt;/div&gt;
&lt;/div&gt;

&lt;/body&gt;
&lt;/html&gt;
</code></pre></details>
---

### **4. 响应式设计**
#### **媒体查询（Media Queries）**
```css
/* 手机端 */
@media (max-width: 480px) {
  .sidebar { display: none; }
  .content { width: 100%; }
}

/* 平板端 */
@media (min-width: 481px) and (max-width: 1024px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
```

#### **相对单位与动态值**
```css
.container {
  width: 90%;           /* 百分比单位 */
  padding: 2rem;        /* 相对于根字体大小（1rem = 16px） */
  font-size: clamp(1rem, 2vw, 1.5rem); /* 动态字体大小 */
}
```

---

### **5. 常用样式属性**
#### **文本与字体**
```css
.text {
  font-family: "Helvetica", sans-serif;
  font-weight: 600;
  line-height: 1.6;
  text-align: justify;
  text-overflow: ellipsis; /* 文本溢出显示省略号 */
  white-space: nowrap;
  overflow: hidden;
}
```

#### **背景与渐变**
```css
.banner {
  background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
  background-image: url("bg.jpg");
  background-size: cover;
  background-position: center;
}
```

---

## 二、选学进阶方向（根据需求扩展）
### **1. 动画与过渡**
#### **关键帧动画**
```css
@keyframes slideIn {
  from { transform: translateX(-100%); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

.element {
  animation: slideIn 0.5s ease-out 0.3s both;
}
```

#### **过渡效果**
```css
.button {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.button:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

---

### **2. CSS 预处理器（Sass）**
```sass
// 变量与嵌套
$primary-color: #3498db;
$spacing: 1rem;

.nav {
  background: $primary-color;
  padding: $spacing;

  ul {
    list-style: none;
    li {
      display: inline-block;
      a {
        color: darken($primary-color, 20%);
      }
    }
  }
}

// Mixin
@mixin center-flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

.container {
  @include center-flex;
}
```

---

### **3. 现代 CSS 特性**
#### **CSS 变量**
```css
:root {
  --main-color: #2ecc71;
  --spacing: 20px;
}

.header {
  color: var(--main-color);
  padding: var(--spacing);
}
```

#### **容器查询（Container Queries）**
```css
.card {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: flex;
    gap: 20px;
  }
}
```

---

### **4. CSS 框架**
#### **Tailwind CSS**
```html
<div class="p-6 max-w-md mx-auto bg-white rounded-xl shadow-lg">
  <h2 class="text-xl font-medium text-gray-800">标题</h2>
  <p class="mt-2 text-gray-600">内容文本...</p>
</div>

```

---

### **5. 性能优化**
#### **减少重绘**
```css
.optimize {
  will-change: transform;  /* 提示浏览器提前优化 */
  transform: translateZ(0);/* 触发 GPU 加速 */
}
```

#### **图片懒加载**
```html
<img src="placeholder.jpg" data-src="image.jpg" loading="lazy">
```

---

## **三、代码示例汇总**
### **BEM 命名规范**
```css
/* Block */
.card { ... }

/* Element */
.card__title { ... }

/* Modifier */
.card--dark { ... }
```

### **暗黑模式适配**
```css
@media (prefers-color-scheme: dark) {
  body {
    background: #1a1a1a;
    color: #fff;
  }
}
```
