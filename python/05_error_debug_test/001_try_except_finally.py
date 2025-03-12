# 程序可能出现错误时，使用try-except-finally语句可以捕获异常并进行处理，并在程序结束时执行finally语句块。
# 语法
# try:
#     # 可能出现错误的代码
# except ExceptionType1 as e1:
#     # 捕获异常1，并进行处理
# except ExceptionType2 as e2:
#     # 捕获异常2，并进行处理
# ......
# finally:
#     # 程序结束时执行的代码

# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# 所以如果上面的错误是下面错误的父类，那么下面的错误永远不可能被执行到

#  提示：出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
# Python内置的logging模块可以非常容易地记录错误信息：logging.exception(e)
import logging
try:
    a = 10/0
except Exception as e:
    logging.exception(e)
finally:
    print("end")


# 抛出异常
# raise Exception
def myabs(value):
    if not isinstance(value, int):
        raise TypeError("参数类型错误，只接受整数")
    if value < 0:
        return -value
    else:
        return value

try:
    print(myabs("a"))
except TypeError as e:
    logging.exception(e)

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型


# ----------raise ... from exception
# 在Python中，raise ... from ... 语法用于在引发异常时指定一个新的异常，并且可以保留原来的异常上下文信息。
# 这是一种更清晰地处理异常的方式，特别适用于在捕获一个异常后需要引发另一个异常的情况。
# 例如：
# try:
#     1 / 0
# except ZeroDivisionError as e:
#     raise ValueError("除零错误") from e

# 在这个例子中，当捕获到 ZeroDivisionError 异常后，代码引发了 ValueError 异常。
# from e 指定了新异常的原因，使得在异常信息中可以看到原始异常的详细信息，从而更容易进行调试和错误跟踪。
# 需要注意的是，如果不想在新异常中包含原始异常的信息，可以使用 raise ... from None 来抑制原始异常的上下文信息。


# 自定义异常
# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
# 自定义错误类型时，最好从Exception类派生。
class MyError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise MyError("自定义异常")
except MyError as e:
    logging.exception(e)