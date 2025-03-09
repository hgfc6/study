# 上下文管理
# 在Python中，上下文管理是一种用于管理资源（如文件、网络连接等）的机制，
# 它确保资源被正确地分配和释放，即使在代码执行过程中发生异常。这一机制主要通过with语句来实现。
# 上下文管理器通常需要实现两个特殊方法：__enter__ 和 __exit__。
# __enter__方法负责返回资源对象，__exit__方法负责释放资源。
# 以下是一个上下文管理器的例子：

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# 使用上下文管理器可以自动打开和关闭文件：

with FileManager('file.txt', 'a') as f:
    f.write('Hello, world!\n')

# 上下文管理器可以自动处理异常，即使在代码执行过程中发生异常。
# 除了自定义上下文管理器，Python还提供了一些内置的上下文管理器，例如open()函数用于文件操作，socket.socket用于网络连接等
