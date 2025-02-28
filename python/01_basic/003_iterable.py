# 迭代器
# 迭代 是指可以依次访问集合中的元素的过程。
# Python 中有两种迭代器：
# 1. 列表迭代器：用于遍历列表或元组中的元素。
# 2. 字典迭代器：用于遍历字典中的键值对。


# 列表迭代器
# 列表迭代器可以用 for 循环来遍历列表或元组中的元素。

# 示例 1：遍历列表
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# 示例 2：遍历元组
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)

# 示例3：遍历字符串
my_string = "hello world"
for char in my_string:
    print(char)

# 字典迭代器
# 字典迭代器可以用 for 循环来遍历字典中的键值对。
# 示例 1：遍历字典键值
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
    print(key, value)

# 示例2 ：遍历字典的键
for key in my_dict:
    print(key)

# 示例3 ：遍历字典的值
for value in my_dict.values():
    print(value)

# 可迭代对象：
# 1. 列表、元组、字符串、字典都是可迭代对象。
# 2. 自定义的类也可以实现可迭代协议，使其成为可迭代对象。
# 3. 迭代器：可以迭代的对象称为迭代器。
# 如何判断一个对象是否是可迭代对象？
# 方法是通过collections.abc模块的Iterable类型判断
# 示例：

# 示例1：判断列表是否是可迭代对象
from collections.abc import Iterable
my_list = [1, 2, 3, 4, 5]
print(isinstance(my_list, Iterable))  # True

