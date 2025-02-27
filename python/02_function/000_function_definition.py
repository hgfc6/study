# 函数定义

# 定义一个函数
# def 函数名(参数列表):
#     函数体
# 调用函数
# 函数名(参数)
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


# 空函数
def empty_func():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

import math

# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny



if __name__ == '__main__':
    x, y = move(100, 100, 60, math.pi / 6)
    print(x, y) # 151.96152422706632 70.0
    # 这只是一种假象，Python函数返回的仍然是单一值
    print(move(100, 100, 60, math.pi / 6)) # (151.96152422706632, 70.0)
    # 返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
    # 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

