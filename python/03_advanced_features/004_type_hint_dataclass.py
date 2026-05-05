"""
Python 进阶补充：类型标注、dataclass、TypedDict。

运行方式：
    python 03_advanced_features/004_type_hint_dataclass.py
"""

from dataclasses import dataclass, field
from typing import TypedDict


class UserPayload(TypedDict):
    """
    TypedDict 用来描述字典的结构。

    它不会在运行时强制校验类型，但 IDE、类型检查工具可以根据它发现问题。
    """

    name: str
    age: int
    tags: list[str]


@dataclass
class User:
    """
    dataclass 适合表示“主要用来存数据”的类。

    Python 会自动生成 __init__、__repr__、__eq__ 等常用方法。
    """

    name: str
    age: int

    # default_factory 用来给可变字段设置默认值。
    # 不要直接写 tags: list[str] = []，否则多个对象会共享同一个列表。
    tags: list[str] = field(default_factory=list)

    def is_adult(self) -> bool:
        """返回用户是否成年。"""

        return self.age >= 18


def build_user(payload: UserPayload) -> User:
    """把普通字典转换成 User 对象。"""

    return User(
        name=payload["name"],
        age=payload["age"],
        tags=payload["tags"],
    )


def average(numbers: list[float]) -> float:
    """
    计算平均值。

    类型标注不会替你处理空列表，所以业务边界仍然要自己检查。
    """

    if not numbers:
        raise ValueError("numbers 不能为空")

    return sum(numbers) / len(numbers)


def main():
    """集中演示类型标注相关写法。"""

    payload: UserPayload = {
        "name": "cjh",
        "age": 18,
        "tags": ["python", "backend"],
    }

    user = build_user(payload)

    print("\n一、dataclass")
    print(user)
    print(f"是否成年: {user.is_adult()}")

    print("\n二、类型标注的函数")
    scores = [88.5, 92.0, 79.5]
    print(f"平均分: {average(scores):.2f}")

    print("\n三、可变默认值的安全写法")
    another_user = User(name="alice", age=20)
    user.tags.append("dataclass")
    print(f"user.tags: {user.tags}")
    print(f"another_user.tags: {another_user.tags}")


if __name__ == "__main__":
    main()
