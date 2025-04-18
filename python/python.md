[**示例代码和输出都是根据 Python 3.13.1**]()

[学习内容参考出处](https://liaoxuefeng.com/books/python/introduction/index.html)
#### 一、Python 必学内容
1. **基础语法**
    - [变量与数据类型](./01_basic/001_data_types_and_variables.py)（整数、浮点数、[字符串](./01_basic/002_String_encoding.py)、布尔值等）
    - 运算符（算术、比较、逻辑、赋值等）
    - 控制结构（[条件语句](./01_basic/004_if_else_and_match.py) `if-else`，[循环语句](./01_basic/005_for_and_while.py) `for`、`while`）
    - 输入输出（`input()`、`print()`）
2. **数据结构**
    - [列表](./01_basic/003_list_and_tuple.py)（`list`）：增删改查、切片、列表推导式
    - [元组](./01_basic/003_list_and_tuple.py)（`tuple`）：不可变序列
    - [字典](./01_basic/006_dict_and_set.py)（`dict`）：键值对操作
    - [集合](./01_basic/006_dict_and_set.py)（`set`）：去重、集合运算
3. **函数**
    - [定义与调用函数](./02_function/001_function_parameter.py)
    - [参数传递](./02_function/001_function_parameter.py)（位置参数、关键字参数、默认参数）
    - 返回值与作用域
    - 匿名函数（`lambda`）
4. **[文件操作](./06_io/io.md)**
    - 文件读写（`open()`、`read()`、`write()`）
    - [上下文管理器](./06_io/004_context_manage.py)（`with` 语句）
5. **[面向对象编程（OOP）](./04_oop/OOP.md)**
    - 类与对象
    - 构造函数（`__init__`）
    - 继承与多态
    - 封装与私有属性
6. **[模块与包](./08_module/module.md)**
    - 导入模块（`import`）
    - 常用标准库（如 `os`、`sys`、`math`、`datetime`）
    - 创建与使用自定义模块
7. [**错误与异常处理**](./05_error_debug_test/error_debug_test.md)
    - `try-except-finally` 结构
    - 自定义异常
8. **常用工具**
    - 列表推导式、字典推导式
    - [生成器与迭代器](./03_advanced_features/002_generators.py)
    - `enumerate()`、`zip()` 等内置函数

---

#### 二、Python 选学内容
1. **高级数据结构**
    - 堆（`heapq`）
    - 队列（`queue`）
    - 链表、栈等自定义数据结构
2. **[函数式编程](./02_function/002_functional_programming.py)**
    - `map()`、`filter()`、`reduce()`
    - 装饰器（`@decorator`）
3. **[并发与并行](./07_process_thread/ProcessAndThread.md)**
    - 多线程（`threading`）
    - 多进程（`multiprocessing`）
    - 异步编程（`asyncio`）
4. **数据库操作**
    - SQLite、MySQL、PostgreSQL 等数据库连接与操作
    - ORM 框架（如 `SQLAlchemy`）
5. **网络编程**
    - 基本网络通信（`socket`）
    - HTTP 请求（`requests` 库）
    - Web 框架（如 `Flask`、`Django`）
6. **数据处理与分析**
    - `NumPy`：数值计算
    - `Pandas`：数据分析
    - `Matplotlib`、`Seaborn`：数据可视化
7. **机器学习与人工智能**
    - `Scikit-learn`：机器学习库
    - `TensorFlow`、`PyTorch`：深度学习框架
    - `NLTK`、`spaCy`：自然语言处理
8. **自动化与脚本**
    - 自动化任务（`os`、`shutil`）
    - 网络爬虫（`BeautifulSoup`、`Scrapy`）
    - 自动化测试（`unittest`、`pytest`）
9. **性能优化**
    - 代码性能分析（`cProfile`）
    - 代码优化技巧
10. **部署与打包**
    - 虚拟环境（`venv`、`conda`）
    - 打包工具（`PyInstaller`、`setuptools`）
    - 部署工具（`Docker`、`Kubernetes`）

---

#### 三、学习建议
1. **循序渐进**：先掌握基础语法，再逐步学习高级内容。
2. **实践为主**：通过项目实战巩固知识。
3. **查阅文档**：熟悉 Python 官方文档和常用库的文档。
4. **参与社区**：加入 Python 社区，交流学习经验。

## Python基础学习后的练手建议

### 一、编程练习题
1. **经典练习题**
   - 完成100道Python基础练习题，涵盖变量、循环、函数等核心知识点[1]
   - 例如：字符串处理、数值计算、列表操作等基础题目[1]

### 二、开源项目推荐
1. **Web开发方向**
   - Flask/Django框架的博客系统
   - 电商网站后台开发（含用户管理、商品管理模块）

2. **数据分析方向**
   - 使用Pandas处理Excel/CSV数据
   - 基于Matplotlib/Seaborn的数据可视化项目

3. **自动化工具**
   - 文件批量处理工具
   - 网页数据爬虫（需遵守robots协议）

### 三、开发环境准备
1. 安装Python3.x + PyCharm/VSCode
2. 配置Git版本控制[2]
3. 建议使用virtualenv创建虚拟环境[2]

### 四、进阶学习路径
1. **算法与数据结构**
   - 实现常见排序算法（冒泡/快排）
   - 链表/二叉树等数据结构实践

2. **项目开发技巧**
   - 学习使用requirements.txt管理依赖
   - 掌握单元测试（unittest/pytest）[4]

### 五、注意事项
1. 从简单项目开始，逐步增加复杂度
2. 每个项目确保有明确的需求文档[4]
3. 推荐通过技术博客记录开发过程[4]


