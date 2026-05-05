# Todo CLI 练手项目

这是一个只使用 Python 标准库实现的命令行 Todo 工具，用来练习：

1. `argparse` 命令行参数
2. `dataclass` 数据建模
3. `json` 文件读写
4. `pathlib` 路径处理
5. 基础 CRUD 思路

## 运行方式

添加任务：

```shell
python todo_cli.py add "学习 Python"
```

查看任务：

```shell
python todo_cli.py list
```

完成任务：

```shell
python todo_cli.py done 1
```

删除任务：

```shell
python todo_cli.py delete 1
```

清空任务：

```shell
python todo_cli.py clear
```

## 文件说明

| 文件 | 说明 |
| --- | --- |
| [todo_cli.py](./todo_cli.py) | Todo CLI 主程序 |
| `todos.json` | 运行时生成的数据文件，不需要提交到 Git |
