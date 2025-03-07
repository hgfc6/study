# 定制类
# python中有诸如__slots__、__len__()等特殊用途的函数，可以帮助我们定制类
# 常见特殊方法
# __init__()：构造函数，在对象创建时调用
from typing import Callable


# __del__()：析构函数，在对象销毁时调用

# __len__()：返回对象长度，如len()函数调用

# __str__()：打印对象时调用，返回字符串
# __repr__()：调试时调用，返回字符串
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 要想两者一直，偷懒的方法是：
class MyClass:
    def __init__(self, name):
        self._name = name
    def __del__(self):
        print("对象已被销毁")
    def __str__(self):
        return f'{self._name} nb666'
    # __repr__ = __str__
my_obj = MyClass("cjh")
print(my_obj) # 输出nb666

# __iter__()：
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# __next__()：# 该方法返回下一个值，直到遇到StopIteration错误时退出循环。
class fibonacci(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a

for n in fibonacci():
    print(n)

# __getitem__()：
# 如果一个类想被用于索引操作，类似list或tuple那样，就必须实现一个__getitem__()方法，该方法返回指定位置的元素。
# fibonacci实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# print(fibonacci()[4]) # TypeError: 'fibonacci' object is not subscriptable
class fibonacci2(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = fibonacci2()
print(f[0]) # 输出5
# list有个神奇的切片方法list[start:end:step]
# fabonacci2却不行，因为没有处理n
# print(f[0:5]) # TypeError: 'slice' object cannot be interpreted as an integer
# 改进方法
class fabonacci3(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        elif isinstance(n, slice):
            start = n.start
            stop = n.stop
            step = n.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = fabonacci3()
print(f[0:5]) # [1, 1, 2, 3, 5]

# __setitem__()：
# 如果一个类想被用于索引赋值操作，类似list那样，就必须实现一个__setitem__()方法，该方法设置指定位置的元素。

# __delitem__()：
# 如果一个类想被用于索引删除操作，类似list那样，就必须实现一个__delitem__()方法，该方法删除指定位置的元素。

# __getattr__()：
# 当我们调用对象不存在的方法时，就会报错
class Student(object):
    def __init__(self, name):
        self._name = name

s = Student("cjh")
# print(s.age) # AttributeError: 'Student' object has no attribute 'age'
# 为了避免这种错误，除了可以加上一个score属性外,还可以实现一个__getattr__()方法，动态返回一个属性
class Student2(object):
    def __getattr__(self, item):
        if item == "age":
            return 20

s = Student2()
print(s.age) # 20

# 也可以返回函数，不过调用方法要变
class Student3(object):
    def __getattr__(self, item):
        if item == "score":
            return lambda: 90

s = Student3()
print(s.score()) # 90
print(s.addr) # None为什么会这样？因为Student3没有定义addr属性，__getattr__()方法默认返回None
# 改进
# def __getattr__(self, item):
#         if item == "score":
#             return lambda: 90
#         raise AttributeError(f"Student3 object has no attribute '{item}'")

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 有什么用？
# 举个例子，假设我们有一个数据库连接池，每个连接都有一个超时时间，如果连接超时，我们就需要重新连接。
# 我们可以定义一个ConnectionPool类，里面有个__init__()方法，用来初始化连接池，里面有个connections属性，用来保存连接对象。
# 然后，我们可以定义一个__getattr__()方法，用来动态返回connections属性，这样，我们就可以通过pool.connections.xxx来访问连接对象了。
# 假设我们还需要设置连接超时时间，我们可以定义一个set_timeout()方法，然后，我们就可以通过pool.connections.set_timeout(10)来设置超时时间了。
# 这样，我们就不需要在ConnectionPool类里写死超时时间，而是通过动态属性来设置。
class ConnectionPool(object):
    def __init__(self):
        self.connections = []
    def __getattr__(self, item):
        if item == "connections":
            return self.connections
        elif item.startswith("set_timeout_"):
            index = int(item.split("_")[1])
            def set_timeout(timeout):
                self.connections[index].timeout = timeout
            return set_timeout
        raise AttributeError(f"ConnectionPool object has no attribute '{item}'")
# 或者根据实例动态生成RestFul API
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users.comments.list.GET.url) # /users/comments/list/GET/url
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！


# __call__()：
# 如果一个类想被当作函数来调用，就必须实现一个__call__()方法，该方法返回一个函数对象。
# 然后，我们就可以通过实例对象调用该函数，就像调用普通函数一样。
class Student4(object):
    def __init__(self, name):
        self._name = name
    def __call__(self):
        print("Hello, %s!" % self._name)

s = Student4("cjh")
s() # 输出Hello, cjh!
# 对实例进行直接调用就好比对一个函数进行调用一样，完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，就模糊了对象和函数的界限。
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 比如函数和我们上面定义的带有__call__()的类实例

print(callable(s)) # True

# 更多特殊方法参考 https://docs.python.org/3/reference/datamodel.html#special-method-names
