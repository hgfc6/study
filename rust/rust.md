# Rust语言学习清单

## 1. **开始学习**
- **安装Rust**
    - 从官方网站下载并安装Rust。
    - 设置开发环境（IDE或文本编辑器）。
- **Hello, World!**
    - 编写并运行你的第一个Rust程序。
- **基本语法**
    - 变量和数据类型
    - 函数
    - 控制流（if, loop, match）

## 2. **数据类型和变量**
- **原始类型**
    - 整数（i8, i16, i32, i64, isize）
    - 浮点数（f32, f64）
    - 布尔值（bool）
    - 字符（char）
- **复合类型**
    - 元组
    - 数组
    - 切片
- **所有权和 borrowing**
  所有权规则
    - 借用规则
    - 生命周期

## 3. **控制流**
- **条件语句**
    - if, else
    - match
- **循环**
    - loop
    - while
    - for
- **错误处理**
    - panic!
    - Result和Option
    - 错误传播

## 4. **函数和闭包**
- **函数定义**
    - 函数参数和返回类型
    - 函数指针
- **闭包**
    - 闭包语法
    - 闭包trait（Fn, FnMut, FnOnce）
- **高阶函数**
    - map, filter, fold
    - 迭代器方法

## 5. **模块和库**
- **模块系统**
    - 定义模块
    - 使用模块
    - 可见性（pub, crate, super, self）
- **库**
    - 创建库
    - 依赖
    - Cargo.toml配置

## 6. **并发**
- **线程**
    - 创建线程
    - 线程同步（Mutex, Arc）
- **异步编程**
    - Futures
    - Async/Await
    - Tokio运行时

## 7. **内存管理**
- **智能指针**
    - Box
    - Rc, RefCell
    - Arc, Mutex
- **垃圾回收**
    - Rust的内存管理模型
    - Drop trait

## 8. **高级主题**
- **宏**
    - 宏规则
    - 宏卫生
- **模式匹配**
    - match表达式
    - if let, while let
- **泛型**
    - 泛型函数
    - 泛型结构体和枚举
    - Trait边界

## 9. **标准库**
- **集合**
    - Vec, HashMap, HashSet
    - 迭代器
- **文件I/O**
    - 读取和写入文件
    - 标准输入输出
- **网络**
    - TCP/IP通信
    - HTTP客户端和服务器

## 10. **测试**
- **单元测试**
    - 编写测试
    - Mocking和Spying
- **集成测试**
    - 端到端测试
    - 测试框架（cargo test）

## 11. **性能优化**
- **代码分割**
    - 动态导入
    - Webpack中的代码分割
- **优化资产**
    - 压缩（UglifyJS, Terser）
    - 图片优化（WebP, AVIF）
- **缓存**
    - Service workers
    - 缓存策略

## 12. **部署和CI/CD**
- **部署**
    - Netlify
    - Vercel
- **CI/CD流水线**
    - GitHub Actions
    - Jenkins

## 13. **安全**
- **常见漏洞**
    - 跨站脚本攻击（XSS）
    - 跨站请求伪造（CSRF）
- **安全编码实践**
    - 输入验证
    - 内容安全策略（CSP）

## 14. **高级主题**
- **WebAssembly**
    - WebAssembly介绍
    - 构建WebAssembly模块
    - 与JavaScript集成
- **渐进式网络应用程序（PWA）**
    - Service workers
    - 背景同步
    - 推送通知
    - Manifest文件
- **无服务器架构**
    - AWS Lambda
    - Firebase Cloud Functions

## 15. **社区和资源**
- **在线社区**
    - Stack Overflow
    - Reddit (r/rust, r/learnprogramming)
- **书籍和课程**
    - "The Rust Programming Language" by Steve Klabnik and Carol Nichols
    - "Rust in Action" by Jim Blandy and Jason Orendorff
    - 在线课程（Udemy, Pluralsight, freeCodeCamp）

## 16. **项目和练习**
- **个人项目**
    - 待办事项应用
    - 天气应用
- **开源贡献**
    - 寻找项目
    - 贡献指南
    - 协作

通过遵循这个详细的学习清单，你将能够系统地掌握Rust，并成为一名熟练的Rust程序员。加油！