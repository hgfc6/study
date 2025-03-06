# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

stu = Student("Alice", 20)
# print(stu.__name)  # 报错，实例变量不能被外部访问
print(stu.get_name())  # 正确，调用get_name()方法获取私有变量
# 同样，修改私有变量也不行，可以通过set_方法修改

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是
# 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
# 所以，仍然可以通过_Student__name来访问__name变量：
print(stu._Student__name)
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

# >>>注意下面错误写法
stu2 = Student("Bob", 21)
stu2.__name = "Charlie"
print(stu2.__name) # 输出Charlie
# 这样写虽然没报错，但是并没有给示例变量的__name属性赋值，只是给stu2新增了一个变量名为__name的属性，并没有修改stu2的__name属性。
print(stu2.get_name()) # 输出Bob，说明__name属性没有被修改



# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 特殊变量的作用主要是用来帮助实现一些语言特性，比如元类（metaclass）、描述符（descriptor）等。


# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问