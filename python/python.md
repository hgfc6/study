# Python 学习清单

当前目录以 Python 3 为主，内容覆盖基础语法、函数、面向对象、I/O、并发、网络、数据库和常见 Web 框架。

参考学习路线：<https://liaoxuefeng.com/books/python/introduction/index.html>

## 一、基础必学

1. 基础语法
   - [变量与数据类型](./01_basic/001_data_types_and_variables.py)
   - [字符串与编码](./01_basic/002_String_encoding.py)
   - [条件判断与 match](./01_basic/004_if_else_and_match.py)
   - [循环语句](./01_basic/005_for_and_while.py)
2. 常用数据结构
   - [列表与元组](./01_basic/003_list_and_tuple.py)
   - [字典与集合](./01_basic/006_dict_and_set.py)
   - [可迭代对象](./01_basic/003_iterable.py)
   - [解包、真假值、浅拷贝与深拷贝](./01_basic/007_unpacking_copy_truthiness.py)
3. 函数
   - [函数定义](./02_function/000_function_definition.py)
   - [函数参数](./02_function/001_function_parameter.py)
   - [函数式编程基础](./02_function/002_functional_programming.py)
   - [闭包与装饰器](./02_function/003_closure_and_decorator.py)
4. 高级特性
   - [列表生成式](./03_advanced_features/001_list_generic.py)
   - [生成器](./03_advanced_features/002_generators.py)
   - [迭代器](./03_advanced_features/003_iterator.py)
   - [类型标注、dataclass、TypedDict](./03_advanced_features/004_type_hint_dataclass.py)
5. 面向对象
   - [OOP 总览](./04_oop/OOP.md)
   - [访问限制](./04_oop/001_access%20_restrictions.py)
   - [继承与多态](./04_oop/002_oop_extends.py)
   - [对象信息](./04_oop/003_get_object_info.py)
   - [ABC 与 Protocol](./04_oop/advanced_features/007_abc_protocol.py)
6. 错误处理与调试
   - [异常处理](./05_error_debug_test/001_try_except_finally.py)
   - [调试、断言、日志](./05_error_debug_test/002_debug_assert_logging_pdb.py)
   - [单元测试](./05_error_debug_test/003_unit_test.py)
   - [文档测试](./05_error_debug_test/004_doc_test.py)
   - [pytest 基础](./05_error_debug_test/005_pytest_basic.py)
7. 文件与 I/O
   - [I/O 总览](./06_io/io.md)
   - [文件读写](./06_io/001_file_read_write.py)
   - [文件和目录操作](./06_io/002_opera_file_and_dir.py)
   - [序列化](./06_io/003_serialization.py)
   - [上下文管理器](./06_io/004_context_manage.py)
8. 模块与包
   - [模块与包](./08_module/module.md)
   - [常用标准库示例](./08_module/001_common_stdlib_examples.py)
   - [常用内置模块](./08_module/commonly_used_modules/commonly_used_built-in_modules.md)
   - [常用第三方模块](./08_module/commonly_used_modules/commonly_used_third_party_%20modules.md)

## 二、进阶主题

1. 并发与并行
   - [进程与线程总览](./07_process_thread/ProcessAndThread.md)
   - [多进程](./07_process_thread/001_multi_process.py)
   - [多线程](./07_process_thread/002_multi_thread.py)
   - [ThreadLocal](./07_process_thread/003_thread_local.py)
   - [分布式进程](./07_process_thread/004_distributed_processes.py)
2. 网络编程
   - [TCP](./09_web/001_tcp.py)
   - [UDP](./09_web/02_udp.py)
3. 数据库
   - [SQLite](./10_connect_db/001_sqlite.py)
   - [MySQL](./10_connect_db/002_mysql.py)
   - [SQLAlchemy](./10_connect_db/003_sqlalchemy.py)
4. 异步编程
   - [协程](./11_async_io/001_coroutine.py)
   - [asyncio 并发、超时、队列](./11_async_io/002_async_io.py)
   - [aiohttp 异步 HTTP 服务](./11_async_io/003_async_http.py)
5. Web 框架
   - [框架总览](./framework/README.md)
   - [Django](./framework/Django/README.md)
   - [Flask](./framework/Flask/README.md)
   - [FastAPI](./framework/FastAPI/README.md)
6. 工程化基础
   - [工程化基础总览](./12_project_engineering/README.md)
   - [日志、配置、命令行参数](./12_project_engineering/001_logging_config_cli.py)
   - [项目结构与依赖管理](./12_project_engineering/002_project_layout_and_dependencies.md)
7. 综合练习
   - [Todo CLI 练手项目](./practice/todo_cli/README.md)

## 三、当前还值得补充的知识点

1. 虚拟环境与依赖管理
   - `venv`
   - `pip`
   - `requirements.txt`
   - `pyproject.toml`
2. 装饰器的更多实战案例
3. 上下文管理器的底层协议
   - `__enter__`
   - `__exit__`
4. 类型标注进阶
   - `Protocol`
   - 泛型
   - 静态类型检查工具
5. 测试体系
   - `pytest`
   - fixture
   - mock
6. 性能分析
   - `timeit`
   - `cProfile`
7. 打包与发布
   - wheel
   - setuptools
8. 常见工程化能力进阶
   - 配置文件解析
   - 分层项目目录
   - 统一异常处理
   - 自动化测试流水线

## 四、练手建议

1. 基础阶段
   - 实现学生信息管理系统
   - 实现命令行待办事项工具
   - 做一组字符串、列表、字典小练习
2. 进阶阶段
   - 写一个文件批量处理脚本
   - 写一个简单爬虫
   - 用 SQLite 做一个小型 CRUD 程序
   - 写一个 JSON 持久化的命令行 Todo 工具
3. 框架阶段
   - 用 Flask 做一个最小博客
   - 用 Django 做一个后台管理 Demo

## 五、建议学习顺序

1. 先把 `01_basic`、`02_function`、`03_advanced_features` 走通。
2. 再补 `04_oop`、`05_error_debug_test`、`06_io`。
3. 然后进入 `07_process_thread`、`09_web`、`10_connect_db`、`11_async_io`。
4. 再学习 `12_project_engineering`，补日志、配置、CLI 等项目基础能力。
5. 最后再看 `framework` 和更偏项目化的内容。

## 六、学习原则

1. 不要只看 `.md`，要同步运行 `.py` 示例。
2. 每学完一个主题，最好自己重写一遍关键例子。
3. 对“函数参数、闭包、装饰器、迭代器、协程”这些抽象点，要主动补小实验。
4. 学框架前先把标准库和语言本身打牢，不然容易只会照着写。
