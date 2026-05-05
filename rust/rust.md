# Rust 学习清单

这个目录当前以入门示例为主，适合按“概念 -> 代码 -> 小项目”的方式推进。

## 已有内容

| 主题 | 说明 | 入口 |
| --- | --- | --- |
| Hello World | 最小可运行程序 | [hello_world/main.rs](./hello_world/main.rs) |
| Hello Cargo | 使用 Cargo 管理项目 | [hello_cargo](./hello_cargo/) |
| Guessing Game | 典型入门练手项目 | [guessing_game](./guessing_game/) |
| General Programming Concepts | 变量、数据类型、函数、控制流等基础主题 | [001_general_programming_concepts](./001_general_programming_concepts/) |

## 一、入门阶段

1. 安装 Rust 工具链
   - `rustup`
   - `cargo`
   - `rustc`
2. 跑通第一个程序
   - `hello_world`
   - `hello_cargo`
3. 理解 Cargo 的基本职责
   - 创建项目
   - 编译和运行
   - 管理依赖
   - 运行测试

## 二、基础语法

1. 变量与可变性
   - `let`
   - `mut`
   - 常量 `const`
   - 变量遮蔽 shadowing
2. 常见数据类型
   - 整数、浮点数、布尔值、字符
   - 元组、数组、切片
3. 函数
   - 参数与返回值
   - 表达式与语句的区别
4. 控制流
   - `if`
   - `loop`
   - `while`
   - `for`
   - `match`

## 三、Rust 最核心的知识点

1. 所有权
   - 值在任意时刻只有一个所有者
   - 离开作用域自动释放
2. 借用
   - 不可变借用 `&T`
   - 可变借用 `&mut T`
   - 不能同时存在可变借用和不可变借用
3. 生命周期
   - 生命周期解决的是“引用能活多久”的问题
   - 先理解规则，再学习显式标注
4. 切片
   - `&str`
   - 数组切片和字符串切片

这部分是 Rust 和其他主流语言差异最大的地方，必须反复结合代码练。

## 四、结构化编程

1. 结构体 `struct`
   - 定义结构体
   - 元组结构体
   - 方法 `impl`
2. 枚举 `enum`
   - 枚举变体
   - `Option<T>`
   - `Result<T, E>`
3. 模式匹配
   - `match`
   - `if let`
   - `while let`

## 五、集合与标准库

1. 常见集合
   - `Vec<T>`
   - `String`
   - `HashMap<K, V>`
2. 迭代器
   - `iter`
   - `into_iter`
   - `iter_mut`
   - `map`、`filter`、`collect`
3. 错误处理
   - `panic!`
   - `Result`
   - `?` 操作符

## 六、模块与工程组织

1. 模块系统
   - `mod`
   - `pub`
   - `use`
   - `crate`
   - `super`
2. 包与 crate
   - 二进制 crate
   - 库 crate
3. `Cargo.toml`
   - 包信息
   - 依赖管理
   - profile 配置

## 七、进阶主题

1. 泛型
   - 泛型函数
   - 泛型结构体
   - 泛型枚举
2. Trait
   - 定义 trait
   - 实现 trait
   - trait bound
3. 生命周期进阶
   - 结构体中的引用
   - 生命周期省略规则
4. 闭包与高阶函数
5. 智能指针
   - `Box<T>`
   - `Rc<T>`
   - `RefCell<T>`
   - `Arc<T>`
   - `Mutex<T>`

## 八、并发与异步

1. 线程
   - `std::thread`
   - `move` 闭包
2. 线程间通信
   - `mpsc` channel
3. 共享状态并发
   - `Mutex`
   - `Arc`
4. 异步编程
   - `async/await`
   - `Future`
   - Tokio 生态

## 九、测试与工具链

1. 单元测试
   - `cargo test`
   - `#[test]`
2. 文档测试
3. 常用工具
   - `cargo fmt`
   - `cargo clippy`
   - `cargo doc`

## 十、练手项目建议

1. 命令行计算器
2. 猜数字游戏扩展版
3. 待办事项 CLI
4. 文本统计工具
5. 简单 HTTP 服务

## 十一、后续建议补充的知识点

当前仓库还可以继续增加这些专题：

1. 所有权与借用的对比案例
2. `String` 和 `&str` 的常见坑
3. `Option` / `Result` 的实战写法
4. trait 对象和动态分发
5. 生命周期标注的典型示例
6. Tokio 异步小项目
7. 单元测试与集成测试示例

## 学习建议

1. 不要跳过所有权、借用和生命周期，这是 Rust 的根基。
2. 每学一个概念，都写一个最小示例验证。
3. 出现编译错误时，先读编译器提示，Rust 的报错通常很有价值。
4. 学到并发和异步后，再回头看所有权，会理解得更深。
