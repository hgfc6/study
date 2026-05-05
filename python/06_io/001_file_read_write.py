# 文件读写
#
# 运行方式：
#     python 06_io/001_file_read_write.py
#
# 这个文件重点演示：
# 1. 文本文件读写
# 2. with 上下文管理器
# 3. read / readline / readlines 的区别
# 4. BytesIO 内存字节流
# 5. 编码参数 encoding

from io import BytesIO
from pathlib import Path


# 使用 __file__ 定位当前脚本所在目录。
# 这样无论你从项目根目录运行，还是从 python/06_io 目录运行，文件路径都稳定。
CURRENT_DIR = Path(__file__).resolve().parent
TEXT_FILE = CURRENT_DIR / "file_runtime_demo.txt"


def write_text_file() -> None:
    """写入文本文件。"""

    # with 会在代码块结束后自动关闭文件，比手动 close 更安全。
    # encoding="utf-8" 明确指定编码，避免不同系统默认编码不一致。
    with TEXT_FILE.open("w", encoding="utf-8") as file:
        file.write("Hello, world!\n")
        file.write("Python 文件读写示例\n")


def read_all() -> None:
    """一次性读取整个文件。"""

    # read() 会把全部内容读入内存，大文件不建议这样处理。
    with TEXT_FILE.open("r", encoding="utf-8") as file:
        content = file.read()
        print("read():")
        print(content)


def read_by_size() -> None:
    """按固定大小分块读取文件。"""

    print("read(size):")

    with TEXT_FILE.open("r", encoding="utf-8") as file:
        while True:
            # 每次最多读取 8 个字符，适合大文件分块处理。
            chunk = file.read(8)

            if not chunk:
                break

            print(repr(chunk))


def read_line_by_line() -> None:
    """逐行读取文件。"""

    print("readline():")

    with TEXT_FILE.open("r", encoding="utf-8") as file:
        while True:
            line = file.readline()

            if not line:
                break

            print(line.strip())


def readlines_demo() -> None:
    """一次性读取所有行，返回列表。"""

    print("readlines():")

    with TEXT_FILE.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    # readlines() 适合小文件；大文件更建议直接 for line in file。
    print(lines)


def bytes_io_demo() -> None:
    """演示内存中的字节流。"""

    print("BytesIO:")

    # BytesIO 不会写入磁盘，常用于测试、网络数据、二进制数据临时处理。
    memory_file = BytesIO()
    memory_file.write("你好，BytesIO".encode("utf-8"))

    # 写完后指针在末尾，读取前要 seek(0) 回到开头。
    memory_file.seek(0)
    content = memory_file.read()

    print(content)
    print(content.decode("utf-8"))

    memory_file.close()


def main() -> None:
    """集中运行所有文件读写示例。"""

    try:
        write_text_file()
        read_all()
        read_by_size()
        read_line_by_line()
        readlines_demo()
        bytes_io_demo()
    finally:
        # 示例文件只用于演示，运行结束后清理，避免污染学习仓库。
        TEXT_FILE.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
