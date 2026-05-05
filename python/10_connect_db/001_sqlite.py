# SQLite 示例
#
# 运行方式：
#     python 10_connect_db/001_sqlite.py
#
# SQLite 是 Python 标准库自带的轻量级数据库，适合学习 SQL、写小工具、做本地缓存。

import sqlite3
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
DB_FILE = CURRENT_DIR / "study_sqlite.db"


def init_table(conn: sqlite3.Connection) -> None:
    """创建用户表。IF NOT EXISTS 可以避免重复运行时报错。"""

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    )


def insert_user(conn: sqlite3.Connection, name: str, password: str) -> None:
    """插入用户。"""

    # SQL 参数必须用占位符传入，不要把变量直接拼到 SQL 字符串里。
    # 这样可以避免 SQL 注入，也能正确处理字符串转义。
    conn.execute(
        "INSERT OR IGNORE INTO user (name, password) VALUES (?, ?)",
        (name, password),
    )


def find_user(conn: sqlite3.Connection, name: str, password: str) -> list[tuple[int, str]]:
    """根据用户名和密码查询用户。"""

    cursor = conn.execute(
        "SELECT id, name FROM user WHERE name = ? AND password = ?",
        (name, password),
    )

    return cursor.fetchall()


def main() -> None:
    """运行一个完整的 SQLite 建表、插入、查询流程。"""

    # with sqlite3.connect(...) 会在正常结束时提交事务，异常时回滚事务。
    with sqlite3.connect(DB_FILE) as conn:
        init_table(conn)
        insert_user(conn, "abc", "password")
        insert_user(conn, "alice", "123456")

        users = find_user(conn, "abc", "password")

    print(f"数据库文件: {DB_FILE}")
    print(f"查询结果: {users}")


if __name__ == "__main__":
    main()
