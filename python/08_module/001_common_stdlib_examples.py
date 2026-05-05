# 常用标准库示例
#
# 运行方式：
#     python 08_module/001_common_stdlib_examples.py
#
# 标准库是 Python 自带的工具箱，优先掌握标准库可以减少不必要的第三方依赖。

import json
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path


CURRENT_DIR = Path(__file__).resolve().parent
JSON_FILE = CURRENT_DIR / "user_profile.json"


def pathlib_demo() -> None:
    """演示 pathlib 路径操作。"""

    print("\n一、pathlib")

    # pathlib 用对象方式处理路径，比字符串拼接更清晰，也能兼容不同操作系统。
    print(f"当前文件: {Path(__file__).name}")
    print(f"当前目录: {CURRENT_DIR}")
    print(f"JSON 文件路径: {JSON_FILE}")


def json_demo() -> None:
    """演示 JSON 序列化和反序列化。"""

    print("\n二、json")

    profile = {
        "name": "cjh",
        "skills": ["python", "flask", "fastapi"],
        "active": True,
    }

    # ensure_ascii=False 可以让中文正常写入文件，而不是变成 Unicode 转义。
    JSON_FILE.write_text(
        json.dumps(profile, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    loaded_profile = json.loads(JSON_FILE.read_text(encoding="utf-8"))
    print(loaded_profile)

    # 示例运行完清理临时文件，避免学习仓库里不断产生无关文件。
    JSON_FILE.unlink(missing_ok=True)


def datetime_demo() -> None:
    """演示日期时间处理。"""

    print("\n三、datetime")

    # 建议在后端系统中优先使用带时区的时间，避免跨地区部署时产生歧义。
    now = datetime.now(timezone.utc)
    tomorrow = now + timedelta(days=1)

    print(f"当前 UTC 时间: {now.isoformat()}")
    print(f"明天 UTC 时间: {tomorrow.isoformat()}")


def counter_demo() -> None:
    """演示 Counter 统计。"""

    print("\n四、Counter")

    words = ["python", "go", "python", "rust", "python", "go"]
    counter = Counter(words)

    print(counter)
    print(f"出现最多的 2 个词: {counter.most_common(2)}")


def main() -> None:
    """集中运行常用标准库示例。"""

    pathlib_demo()
    json_demo()
    datetime_demo()
    counter_demo()


if __name__ == "__main__":
    main()
