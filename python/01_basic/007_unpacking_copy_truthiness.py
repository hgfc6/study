"""
Python 基础补充：解包、真假值判断、浅拷贝与深拷贝。

运行方式：
    python 01_basic/007_unpacking_copy_truthiness.py
"""

from copy import deepcopy


def demo_unpacking():
    """演示序列解包和扩展解包。"""

    print("\n一、解包")

    point = (10, 20)

    # 左侧变量数量必须和右侧元素数量一致，否则会抛 ValueError。
    x, y = point
    print(f"坐标 x={x}, y={y}")

    numbers = [1, 2, 3, 4, 5]

    # 星号变量会收集剩余元素，结果总是 list。
    first, *middle, last = numbers
    print(f"第一个元素: {first}")
    print(f"中间元素: {middle}")
    print(f"最后一个元素: {last}")

    user = {"name": "cjh", "age": 18}

    # 字典解包经常用于函数调用，键名必须能对应函数参数名。
    def show_user(name, age):
        print(f"用户: {name}, 年龄: {age}")

    show_user(**user)


def demo_truthiness():
    """演示 Python 中常见对象的真假值。"""

    print("\n二、真假值判断")

    values = [
        0,
        1,
        "",
        "hello",
        [],
        [1, 2, 3],
        {},
        {"name": "cjh"},
        None,
    ]

    # 空字符串、空容器、0、None 在条件判断中都被视为 False。
    for value in values:
        print(f"{value!r:>16} -> {bool(value)}")

    name = ""

    # 常见写法：当变量为空时给默认值。
    display_name = name or "匿名用户"
    print(f"显示名称: {display_name}")


def demo_copy():
    """演示赋值、浅拷贝、深拷贝的区别。"""

    print("\n三、赋值、浅拷贝、深拷贝")

    original = [["Python", "Go"], ["MySQL", "Redis"]]

    # 赋值不会创建新对象，alias 和 original 指向同一个列表。
    alias = original

    # 浅拷贝只复制第一层列表，内部的子列表仍然共用。
    shallow = original.copy()

    # 深拷贝会递归复制内部对象，适合复制嵌套数据。
    deep = deepcopy(original)

    original[0].append("Rust")

    print(f"原始数据: {original}")
    print(f"直接赋值: {alias}")
    print(f"浅拷贝:   {shallow}")
    print(f"深拷贝:   {deep}")

    # 判断对象是否是同一个对象，用 is；判断值是否相等，用 ==。
    print(f"alias is original: {alias is original}")
    print(f"shallow == original: {shallow == original}")


def main():
    """把三个演示集中起来，方便直接运行本文件。"""

    demo_unpacking()
    demo_truthiness()
    demo_copy()


if __name__ == "__main__":
    main()
