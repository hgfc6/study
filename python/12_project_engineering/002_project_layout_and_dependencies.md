# 项目结构与依赖管理

这个文档用于补充 Python 项目从脚本到工程时需要掌握的基础能力。

## 一、推荐目录结构

一个小型 Python 项目可以按下面这样组织：

```text
my_project/
    README.md
    pyproject.toml
    requirements.txt
    src/
        my_project/
            __init__.py
            main.py
            config.py
            services.py
    tests/
        test_services.py
```

说明：

1. `README.md`：说明项目用途、安装方式、运行方式。
2. `pyproject.toml`：现代 Python 项目的统一配置文件。
3. `requirements.txt`：记录运行依赖，适合简单项目。
4. `src/`：存放真正的业务代码。
5. `tests/`：存放测试代码。

## 二、虚拟环境

虚拟环境用于隔离不同项目的依赖。

Windows PowerShell：

```shell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

macOS / Linux：

```shell
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

退出虚拟环境：

```shell
deactivate
```

## 三、依赖文件

简单项目可以使用 `requirements.txt`：

```text
Flask>=3.0
SQLAlchemy>=2.0
pytest>=8.0
```

安装依赖：

```shell
pip install -r requirements.txt
```

导出当前环境依赖：

```shell
pip freeze > requirements.txt
```

注意：

1. 学习项目可以用 `requirements.txt`。
2. 正式项目更建议学习 `pyproject.toml`。
3. 不要把 `.venv` 提交到 Git。

## 四、pyproject.toml 示例

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "A small Python project"
requires-python = ">=3.11"
dependencies = [
    "Flask>=3.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
```

## 五、配置管理建议

不要把密码、Token、数据库账号直接写进源码。

推荐优先级：

1. 命令行参数：适合临时覆盖配置。
2. 环境变量：适合部署环境。
3. 配置文件：适合保存非敏感默认配置。
4. 代码默认值：适合学习示例和兜底。

## 六、提交前检查清单

1. 能否从 README 找到运行方式。
2. 是否有明确依赖文件。
3. 是否避免提交 `.venv`、`__pycache__`、临时数据库。
4. 是否能运行基础测试。
5. 是否把敏感配置放在环境变量里。
