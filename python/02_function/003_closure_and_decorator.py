"""
Python 函数补充：闭包与装饰器。

运行方式：
    python 02_function/003_closure_and_decorator.py
"""

from functools import wraps
from time import perf_counter


def make_counter(start=0):
    """
    创建一个计数器函数。

    闭包的核心：内部函数记住了外层函数已经结束后的局部变量。
    """

    count = start

    def counter():
        # nonlocal 表示这里修改的是外层函数 make_counter 中的 count。
        # 如果不写 nonlocal，Python 会把 count 当成本地变量，导致读取时报错。
        nonlocal count
        count += 1
        return count

    return counter


def timer(func):
    """
    统计函数执行耗时的装饰器。

    装饰器本质上是一个函数：接收旧函数，返回新函数。
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # *args 和 **kwargs 让装饰器可以适配任意参数形式的函数。
        start = perf_counter()
        result = func(*args, **kwargs)
        cost = perf_counter() - start
        print(f"{func.__name__} 执行耗时: {cost:.6f} 秒")
        return result

    # wraps 会保留原函数的名称、文档字符串等元信息，调试时很有用。
    return wrapper


def require_positive(func):
    """检查参数必须为正数的装饰器，用来演示装饰器也能做参数校验。"""

    @wraps(func)
    def wrapper(number):
        if number <= 0:
            raise ValueError("number 必须是正数")
        return func(number)

    return wrapper


@timer
@require_positive
def factorial(number):
    """计算阶乘。这里故意用循环，便于初学者理解。"""

    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


def main():
    """演示闭包和装饰器的实际效果。"""

    print("\n一、闭包")
    counter = make_counter(start=10)
    print(counter())
    print(counter())
    print(counter())

    print("\n二、装饰器")
    print(f"5 的阶乘: {factorial(5)}")

    print("\n三、装饰器保留原函数信息")
    print(f"函数名称: {factorial.__name__}")
    print(f"函数说明: {factorial.__doc__}")


if __name__ == "__main__":
    main()
