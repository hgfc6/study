# pytest 基础示例
#
# 运行方式一，直接运行普通示例：
#     python 05_error_debug_test/005_pytest_basic.py
#
# 运行方式二，使用 pytest 运行测试：
#     pytest 05_error_debug_test/005_pytest_basic.py
#
# pytest 会自动发现 test_ 开头的函数，并把它们当成测试用例执行。

try:
    import pytest
except ImportError:
    # 直接运行本文件不依赖 pytest；只有执行 pytest 命令时才需要安装它。
    pytest = None


def divide(a: float, b: float) -> float:
    """除法函数，用于演示正常断言和异常断言。"""

    if b == 0:
        raise ValueError("除数不能为 0")

    return a / b


def normalize_name(name: str) -> str:
    """清理用户名：去掉首尾空格，并统一转成小写。"""

    return name.strip().lower()


def test_divide_success() -> None:
    """测试正常除法结果。"""

    assert divide(10, 2) == 5


def test_divide_zero() -> None:
    """测试异常场景。"""

    if pytest is None:
        raise RuntimeError("请先安装 pytest：pip install pytest")

    # pytest.raises 用来断言某段代码会抛出指定异常。
    with pytest.raises(ValueError, match="除数不能为 0"):
        divide(10, 0)


def test_normalize_name() -> None:
    """用循环模拟多组输入，pytest 会把断言失败位置打印出来。"""

    cases = [
        (" Alice ", "alice"),
        ("BOB", "bob"),
        (" cJh ", "cjh"),
    ]

    for raw_name, expected in cases:
        assert normalize_name(raw_name) == expected


def main() -> None:
    """直接运行时，展示被测试函数的普通用法。"""

    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"normalize_name(' cJh ') = {normalize_name(' cJh ')}")
    print("如需运行测试，请执行：pytest 05_error_debug_test/005_pytest_basic.py")


if __name__ == "__main__":
    main()
