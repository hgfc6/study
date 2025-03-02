# 函数式编程

# 函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
# 因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
# 而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
#
# Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。

# ----------高阶函数
# 函数本身也可以赋值给变量，即：变量可以指向函数。由此引申出高阶函数。
a = abs
print(a(-10))
# 所谓高阶函数，就是能够接受函数作为参数或者返回函数的函数。

# 常用内建高阶函数
# 》》》map()《《《
# map()函数接收两个参数，一个是函数，一个是可迭代对象，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 例如：
def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 》》》reduce()《《《
# reduce()函数接收两个参数，一个是函数，一个是可迭代对象，reduce把函数作用在序列的元素上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，直到序列的最后一个元素。
# 例如：
from functools import reduce
def add(x, y):
    return x + y
r = reduce(add, [1, 2, 3, 4, 5])
print(r)  # 15

# 》》》filter()《《《
# filter()函数接收两个参数，一个是函数，一个是可迭代对象，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
# 例如：
def is_odd(n):
    return n % 2 == 1
r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))  # [1, 3, 5, 7, 9]

# 》》》sorted()《《《
# sorted() 函数可以对任意可迭代对象进行排序操作，默认是升序排序。
# 例如：
r = sorted([36, 5, -12, 9, 21])
print(r)  # [-12, 5, 9, 21, 36]
# 可以提供自定义的键函数来自定义排序顺序，并且
# reverse 标志可以设置为按降序请求结果。
r = sorted([36, 5, -12, 9, 21], key=abs, reverse=True) # 按绝对值排序，倒序输出
print(r)  # [36, 21, 9, 5, -12]


# ----------返回函数
# 加入不想立即获取函数的结果，而是希望在稍后某个时刻再调用该函数，就可以使用返回函数的方式。
# 例如：
def lazy_sum(*args):
    def sum():
        num_sum = 0
        for n in args:
            num_sum += n
        return num_sum
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f())  # 25


# ----------闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，这就形成了闭包，闭包用起来简单，实现起来可不容易。
# 闭包就是返回函数的函数，即一个函数内部定义了另一个函数，并且这个函数使用了外层函数的变量。
# 需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())  # 9 9 9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

# ----------nonlocal
# 闭包如果对外层变量赋值，由于Python解释器会把x当作函数fn()的局部变量，它会报错
# def inc():
#     x = 0
#     def fn():
#         # nonlocal x
#         x = x + 1
#         return x
#     return fn
# f = inc()
# print(f()) # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
# 原因是Python解释器把x当作局部变量，而非nonlocal x，所以会报错。
# 解决方法是使用nonlocal关键字声明x为nonlocal变量，这样解释器就不会把x当作局部变量，而是把它当作外层函数的变量。
def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn
f = inc()
print(f()) # 1
print(f()) # 2
print(f()) # 3


# ----------匿名函数
# 匿名函数即没有名字的函数，可以直接使用lambda表达式创建
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))  # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。


# ----------装饰器 Decorator
# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log # 把@log放到now()函数的定义处，相当于执行了语句：log(now)
def now():
    print('2025-03-02')

now()

# ----------偏函数
# 偏函数（Partial function）是指把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
# 调用这个新函数会更简单。
# 例如，我们要创建一个函数int2()，可以把一个字符串转换为整数，但是，如果字符串不是一个整数，会报错。
# 我们可以用偏函数int2 = partial(int, base=2)来固定参数base为2，这样，无论传入的字符串是什么，都可以转换为整数。
from functools import partial
int2 = partial(int, base=2)
print(int2('1000000')) # 4096
print(int2('1010101')) # 435
# 这里，partial()函数接受一个函数和一些参数，返回一个新的函数，新函数的参数列表是原函数的参数列表，
