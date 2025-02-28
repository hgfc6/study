# 生成器 Iterator
# 为什么要生成器：
# 1. 节省内存，避免创建大量的对象
# 2. 迭代器协议可以更高效的处理数据
# 3. 延迟计算，只有在需要时才生成数据，可以节省内存和时间
# 4. 迭代器协议可以更容易的实现并行计算


# 生成器是一种特殊的迭代器，它可以生成一系列值，但不必一次性生成所有值。
# 他和生成式的区别是
# 1：生成式是一种表达式，它一次性生成所有值，而生成器是一种迭代器，它生成值一个个返回。
# 1：生成式用[]表示，而生成器用()表示。

# 定义生成器函数
# 1. 使用yield关键字来定义生成器函数
# 2. yield关键字会暂停函数的执行，并返回一个值，下一次调用生成器函数时，函数会从上次暂停的地方继续执行。
# 3. 生成器函数只能使用yield关键字，不能使用return关键字。

# 例子：斐波那契数列
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a, b

fi =fibonacci(10)
# 调用生成器函数 next(fi)或者使用for in
for i in fibonacci(10):
    print(i)
# 输出 0 1 1 2 3 5 8 13 21 34

# for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
try:
    while True:
        print(next(fi))
except StopIteration as e:
    print(e.value)
# 输出 0 1 1 2 3 5 8 13 21 34 (55, 89)