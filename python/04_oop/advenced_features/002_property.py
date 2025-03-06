# 绑定属性时不能乱填，否则会出问题
# 我们可以用方法来限制并判断参数的传递，使用时用方法设置属性值，但是略显复杂

# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？答案是有的，这就是 property 装饰器的作用。
# @property装饰器就是负责把一个方法变成属性调用的
class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 90
# s.score = "123" # ValueError('score must be an integer!')
# s.score = 150 # ValueError('score must between 0 ~ 100!')
# 把一个getter方法变成属性，只需要加上@property就可以了
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student2:
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2025 -self._birth

s2 = Student2()
s2.birth = 1999
print(s2.age) # 26
# s2.age = 25 # AttributeError: property 'age' of 'Student2' object has no setter

# 要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：

# class Student(object):
#     # 方法名称和实例变量均为birth:
#     @property
#     def birth(self):
#         return self.birth
# 这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用self.birth()，造成无限递归，最终导致栈溢出报错RecursionError。
