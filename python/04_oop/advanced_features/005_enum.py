# 枚举类

from enum import Enum, unique

Week = Enum('Week', ('One', 'Two'))
print(Week.One)

# 遍历
for name, member in Week.__members__.items():
    print(name, '=>', member)

# 果需要更精确地控制枚举类型，可以从Enum派生出自定义类
@unique # unique装饰器可以帮助我们检查保证没有重复值
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED) # Color.RED
print(Color.GREEN.value) # 2

# 可以有多种方式访问枚举值
print(Color.RED) # Color.RED
print(Color['RED']) # Color.RED
print(Color(1)) # Color.RED