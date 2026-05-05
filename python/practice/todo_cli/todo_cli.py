# Todo CLI 练手项目
#
# 运行示例：
#     python todo_cli.py add "学习 Python"
#     python todo_cli.py list
#     python todo_cli.py done 1
#     python todo_cli.py delete 1
#
# 这个项目只使用标准库，适合练习命令行参数、JSON 文件读写和基础 CRUD。

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "todos.json"


@dataclass
class Todo:
    """Todo 数据模型。"""

    id: int
    title: str
    done: bool = False


def load_todos() -> list[Todo]:
    """从 JSON 文件读取任务列表。"""

    if not DATA_FILE.exists():
        return []

    raw_items = json.loads(DATA_FILE.read_text(encoding="utf-8"))

    # JSON 读出来的是 dict，需要转换回 Todo 对象，后续代码才更清晰。
    return [Todo(**item) for item in raw_items]


def save_todos(todos: list[Todo]) -> None:
    """把任务列表保存到 JSON 文件。"""

    raw_items = [asdict(todo) for todo in todos]

    DATA_FILE.write_text(
        json.dumps(raw_items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def next_id(todos: list[Todo]) -> int:
    """生成下一个任务 ID。"""

    if not todos:
        return 1

    return max(todo.id for todo in todos) + 1


def add_todo(title: str) -> None:
    """添加任务。"""

    todos = load_todos()
    todo = Todo(id=next_id(todos), title=title)
    todos.append(todo)
    save_todos(todos)

    print(f"已添加任务 #{todo.id}: {todo.title}")


def list_todos() -> None:
    """查看所有任务。"""

    todos = load_todos()

    if not todos:
        print("暂无任务")
        return

    for todo in todos:
        status = "done" if todo.done else "todo"
        print(f"#{todo.id} [{status}] {todo.title}")


def mark_done(todo_id: int) -> None:
    """把指定任务标记为完成。"""

    todos = load_todos()

    for todo in todos:
        if todo.id == todo_id:
            todo.done = True
            save_todos(todos)
            print(f"已完成任务 #{todo.id}: {todo.title}")
            return

    print(f"未找到任务 #{todo_id}")


def delete_todo(todo_id: int) -> None:
    """删除指定任务。"""

    todos = load_todos()
    remaining = [todo for todo in todos if todo.id != todo_id]

    if len(remaining) == len(todos):
        print(f"未找到任务 #{todo_id}")
        return

    save_todos(remaining)
    print(f"已删除任务 #{todo_id}")


def clear_todos() -> None:
    """清空所有任务。"""

    save_todos([])
    print("已清空所有任务")


def build_parser() -> argparse.ArgumentParser:
    """构建命令行解析器。"""

    parser = argparse.ArgumentParser(description="标准库实现的 Todo CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="添加任务")
    add_parser.add_argument("title", help="任务标题")

    subparsers.add_parser("list", help="查看任务")

    done_parser = subparsers.add_parser("done", help="完成任务")
    done_parser.add_argument("id", type=int, help="任务 ID")

    delete_parser = subparsers.add_parser("delete", help="删除任务")
    delete_parser.add_argument("id", type=int, help="任务 ID")

    subparsers.add_parser("clear", help="清空任务")

    return parser


def main() -> None:
    """程序入口。"""

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        add_todo(args.title)
    elif args.command == "list":
        list_todos()
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "delete":
        delete_todo(args.id)
    elif args.command == "clear":
        clear_todos()
    else:
        # 正常情况下不会走到这里；保留兜底分支，便于以后扩展命令。
        parser.error(f"未知命令: {args.command}")


if __name__ == "__main__":
    main()
