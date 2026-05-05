# MySQL 示例
#
# 运行方式：
#     python 10_connect_db/002_mysql.py
#
# 默认不会硬编码连接本机 MySQL。你需要先设置环境变量：
#     set MYSQL_HOST=127.0.0.1
#     set MYSQL_PORT=3306
#     set MYSQL_USER=root
#     set MYSQL_PASSWORD=123456
#     set MYSQL_DATABASE=cjh

import os
from contextlib import closing


def get_mysql_config() -> dict[str, str | int]:
    """从环境变量读取 MySQL 配置。"""

    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", ""),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", ""),
    }


def validate_config(config: dict[str, str | int]) -> bool:
    """检查必要配置是否存在。"""

    required_keys = ["user", "password", "database"]
    missing = [key for key in required_keys if not config[key]]

    if missing:
        print(f"缺少 MySQL 环境变量: {', '.join(missing)}")
        print("示例默认跳过真实连接，避免误连本机数据库。")
        return False

    return True


def main() -> None:
    """演示 MySQL 连接、建表、插入和查询。"""

    try:
        import mysql.connector
    except ImportError:
        print("未安装 mysql-connector-python，请先执行：pip install mysql-connector-python")
        return

    config = get_mysql_config()

    if not validate_config(config):
        return

    # closing 确保连接和游标最终会关闭，避免异常时资源泄漏。
    with closing(mysql.connector.connect(**config)) as conn:
        with closing(conn.cursor()) as cursor:
            # 学习示例使用 IF NOT EXISTS，避免重复运行时报表已存在。
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS user (
                    id VARCHAR(20) PRIMARY KEY,
                    name VARCHAR(20) NOT NULL
                )
                """
            )

            # MySQL 驱动使用 %s 作为占位符，不是 SQLite 的 ?。
            cursor.execute(
                "INSERT IGNORE INTO user (id, name) VALUES (%s, %s)",
                ("1", "Michael"),
            )

            cursor.execute("SELECT id, name FROM user WHERE id = %s", ("1",))
            rows = cursor.fetchall()

        conn.commit()

    print(f"查询结果: {rows}")


if __name__ == "__main__":
    main()
