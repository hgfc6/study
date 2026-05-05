# 抽象基类 ABC 与 Protocol 示例
#
# 运行方式：
#     python 04_oop/advanced_features/007_abc_protocol.py
#
# ABC 适合“强约束”：子类必须显式继承并实现抽象方法。
# Protocol 适合“鸭子类型”：对象只要长得像，就可以被类型检查器视为满足接口。

from abc import ABC, abstractmethod
from typing import Protocol


class Storage(ABC):
    """抽象基类：定义存储接口。"""

    @abstractmethod
    def save(self, key: str, value: str) -> None:
        """保存数据。子类必须实现。"""

    @abstractmethod
    def load(self, key: str) -> str | None:
        """读取数据。子类必须实现。"""


class MemoryStorage(Storage):
    """内存存储实现。"""

    def __init__(self) -> None:
        # 用字典模拟数据库，适合演示接口设计。
        self._data: dict[str, str] = {}

    def save(self, key: str, value: str) -> None:
        self._data[key] = value

    def load(self, key: str) -> str | None:
        return self._data.get(key)


class Sender(Protocol):
    """Protocol：只要求对象拥有 send 方法。"""

    def send(self, message: str) -> None:
        """发送消息。"""


class EmailSender:
    """没有继承 Sender，但方法签名符合 Sender 协议。"""

    def send(self, message: str) -> None:
        print(f"发送邮件: {message}")


class SmsSender:
    """另一个符合 Sender 协议的实现。"""

    def send(self, message: str) -> None:
        print(f"发送短信: {message}")


def save_token(storage: Storage, token: str) -> None:
    """使用抽象基类作为参数类型。"""

    storage.save("token", token)


def notify(sender: Sender, message: str) -> None:
    """使用 Protocol 作为参数类型。"""

    sender.send(message)


def main() -> None:
    """演示 ABC 和 Protocol 的使用方式。"""

    print("\n一、ABC 抽象基类")

    storage = MemoryStorage()
    save_token(storage, "abc123")
    print(f"读取 token: {storage.load('token')}")

    print("\n二、Protocol 协议")

    notify(EmailSender(), "系统上线")
    notify(SmsSender(), "验证码 123456")


if __name__ == "__main__":
    main()
