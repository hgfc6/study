# 调试代码是虽然可以用print打印结果，但是后续还要删除，所以有了一下几种方式来调试代码：

# 断言 assert
# 语法：assert expression, message
# 作用：当expression为False时，触发AssertionError异常，并输出message。
# 适用场景：用于检查输入参数是否合法，或者检查函数的返回值是否符合预期。

def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), "参数类型错误"
    return a + b
# print(add(2, '4')) # AssertionError: 参数类型错误
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert


# 日志 logging
# 语法：logging.debug(message)、logging.info(message)、logging.warning(message)、logging.error(message)
# 作用：输出日志信息，可以指定日志级别，默认级别为warning。
# 适用场景：用于输出程序运行过程中的信息，便于跟踪程序运行情况。

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s') # 设置日志格式
# filename 将日志输出到文件
# filemode 'w' 覆盖原文件，'a' 追加到文件末尾
# format 日志格式 '%(asctime)s - %(levelname)s - %(message)s'
# datefmt 时间格式 '%Y-%m-%d %H:%M:%S'
# style 日志格式风格 '%' 或 '{'
# level 日志级别 logging.DEBUG、logging.INFO、logging.WARNING、logging.ERROR、logging.CRITICAL
# handlers 日志处理器 输出到文件、输出到控制台
# stream 输出到屏幕 sys.stderr
# force 强制刷新 True/False
# encoding 日志编码
# errors 错误处理方式 'ignore'、'replace'、'strict'

def add(a, b):
    logging.debug("a = %s, b = %s" % (a, b))
    return a + b

print(add(2, 3)) # 2025-03-09 14:56:34,702 - DEBUG - a = 2, b = 3



# 调试 pdb
# 语法：import pdb; pdb.set_trace()
# 作用：启动Python调试器，可以设置断点、单步调试、查看变量值、执行代码、退出程序等。
# 适用场景：用于检查程序运行过程中出现的错误，或者需要单步调试程序。

import pdb

def add(a, b):
    pdb.set_trace() # 设置断点
    return a + b

print(add(2, 3)) # 程序运行到这里会自动暂停，等待调试器命令。输入命令：n（单步执行）、c（继续执行）、q（退出程序）


# 本地IDEA调试
# vscode、pycharm、sublime text等都可以设置断点、单步调试、查看变量值、执行代码、退出程序等。

