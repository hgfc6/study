# IT易筋经

一个按技术方向拆分的自学仓库，用来沉淀文档、示例代码和小型练手项目。

## 项目定位

- 不是单一业务项目，而是多语言、多方向的学习资料仓库。
- 每个目录尽量同时包含两类内容：知识笔记 + 可运行示例。
- 后续优化方向不是单纯“继续堆代码”，而是把知识结构、入口导航、练习路径整理清楚。

## 项目结构

| 模块 | 说明 | 入口 |
| --- | --- | --- |
| `algorithm` | 数据结构与算法笔记、排序示例 | [算法目录](./algorithm/README.md) |
| `front` | 前端基础与框架，当前包含 HTML、CSS、JavaScript、Vue | [前端总览](./front/README.md) |
| `python` | Python 基础、进阶、并发、Web、数据库、框架 | [Python 学习清单](./python/python.md) |
| `golang` | Go 基础语法、容器、接口、并发、Gin、Gorm、go-zero | [Golang 学习记录](./golang/README.md) |
| `rust` | Rust 入门示例与学习路线 | [Rust 学习清单](./rust/rust.md) |
| `pictures` | 思维导图和配图素材 | [图片目录](./pictures/) |

## 当前内容分布

### 前端

| 方向 | 状态 | 入口 |
| --- | --- | --- |
| HTML | 已有文档和示例 | [html.md](./front/html/html.md) |
| CSS | 已有文档和示例 | [css.md](./front/css/css.md) |
| JavaScript | 已有文档和示例 | [javascript.md](./front/javascript/javascript.md) |
| Vue | 内容最完整，含基础、组件、脚手架示例 | [Vue.md](./front/vue/Vue.md) |
| React | 规划中 | 暂无 |

### 后端与语言

| 方向 | 状态 | 入口 |
| --- | --- | --- |
| Python | 结构较完整，已经拆到专题目录 | [python.md](./python/python.md) |
| Golang | 代码示例很多，统一导航还可以继续加强 | [README.md](./golang/README.md) |
| Rust | 已有入门示例，知识图谱还需要持续补全 | [rust.md](./rust/rust.md) |
| Java | 规划中 | 暂无 |

### 数据库与中间件

当前在根 README 中还没有形成独立文档入口，后续建议逐步补齐：

- MySQL
- PostgreSQL
- SQLite
- Redis
- Elasticsearch
- MongoDB
- InfluxDB
- Prometheus

## 推荐学习顺序

1. 先选一门主语言，优先把基础语法、数据结构、函数、模块和错误处理走通。
2. 同时补 `algorithm`，把数组、链表、栈、队列、排序、查找这些基础题型串起来。
3. 前端方向可以按 `HTML -> CSS -> JavaScript -> Vue` 推进。
4. 后端方向可以按 `语言基础 -> Web 框架 -> 数据库 -> 并发/性能` 推进。
5. 每学完一个主题，都补一个最小可运行示例，避免只有笔记没有反馈。

## 仓库当前最值得优化的点

- 根入口存在缺失链接，导致已有内容无法从首页直达。
- 有些目录代码很多，但缺总览文档，不利于复习。
- 个别知识文档有内容串台或来源残留，影响系统性。
- 命名风格还不完全统一，后续可以逐步规范。

## 下一步建议

建议按下面的顺序继续迭代：

1. 先补“总览文档缺失”的模块，例如 `algorithm`、`front`、数据库方向。
2. 再给每个大模块补“学习路线 + 知识点索引 + 对应示例链接”。
3. 最后再补更多知识点和练手案例，这样新增内容不会失控。
