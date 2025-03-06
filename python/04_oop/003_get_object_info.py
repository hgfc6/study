# 获取对象信息
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)
# 判断对象类型
print(type(p1)) # <class '__main__.Person'>
print(type(p2)) # <class '__main__.Person'>
print(type(p1) == Person) # True
print(type(p1) == type(p2)) # True
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
import types
def my_func():
    pass
print(type(my_func) == types.FunctionType) # True
print(type(p1.say_hello) == types.MethodType) # True
print(type(abs) == types.BuiltinFunctionType) # True
print(type(lambda x: x+1) == types.LambdaType) # True
#----------------------------------------------------------------------------------------------

# 判断继承关系
# issubclass()函数用于判断一个类是否是另一个类的子类
print(issubclass(Person, object)) # True
# isinstance()函数用于判断一个对象是否是某个类或者其子类的实例
print(isinstance(p1, Person)) # True
#----------------------------------------------------------------------------------------------

# dir() 获得一个对象的所有属性和方法
print(dir(p1)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'say_hello']
print(dir("hello")) # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#----------------------------------------------------------------------------------------------

# hasattr() 用于判断一个对象是否有某个属性
print(hasattr(p1, "name")) # True
print(hasattr(p1, "gender")) # False

# getattr() 用于获取一个对象的属性值，可以设置默认值，不加默认值时如果属性不存在会抛出AttributeError异常
print(getattr(p1, "name")) # Alice
print(getattr(p1, "gender", "Unknown")) # Unknown

# setattr() 用于设置一个对象的属性值
setattr(p1, "gender", "Female")
print(p1.gender) # Female
#----------------------------------------------------------------------------------------------

# 实例属性和类属性
# 实例属性是指每个实例对象独有的属性，类属性是指所有实例对象共享的属性
# 实例属性可以通过实例对象来访问，类属性可以通过类来访问
class Dog(object):
    kind = "canine" # 类属性

d1 = Dog()
d2 = Dog()
print(d1.kind) # canine
print(d2.kind) # canine
print(Dog.kind) # canine
d1.kind = "corgi" # 给实例设置与类属性同名的属性值，实例属性优先级更高
print(d1.kind) # corgi
print(d2.kind) # canine