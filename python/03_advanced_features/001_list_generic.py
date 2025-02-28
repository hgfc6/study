# 列表生成式

# 列表生成式是一种简洁的创建列表的方式，它可以根据一个表达式来创建列表。

# 语法：
# [expression for item in iterable if condition]

# expression表达式：
# 一个表达式可以是任何合法的Python表达式，可以是变量、函数调用、算术运算、比较运算等等。
# for前面的部分是一个表达式，它必须根据x计算出一个结果，因此for之前的if必须加else，否则会报错

# iterable迭代对象：
# 迭代对象可以是任何可迭代对象，如列表、元组、字符串、字典等。

# condition条件：
# 条件是可选的，可以用来过滤掉不符合条件的元素。
# for后面的if是一个筛选条件，不能带else，否则如何筛选

# 示例：
# 以下代码使用列表生成式创建了一个列表，其中包含1到10的平方：

squares = [x**2 for x in range(1, 11)]
print(squares) # 输出： [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 以下代码
my_str = [s.upper() for s in 'abcdefg']
print(my_str) # 输出 ['A', 'B', 'C', 'D', 'E', 'F', 'G']
