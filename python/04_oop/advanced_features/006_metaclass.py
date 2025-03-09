# 创建对象时，除了使用class ClassName(object)外还可以直接使用type()函数来创建对象。
# type()函数可以创建出任何类的实例，并可以接收一个参数，即类的属性和方法。
# 例如，我们可以用type()函数创建出一个自定义的元类：

def fn(self, name='world'):
    print('Hello, %s!' % name)

MyType = type('MyType', (object,), dict(hello=fn))
m = MyType()
m.hello()  # Output: Hello, world!

# 动态语言本身支持运行期动态创建类
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# meteclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 太难，暂时跳过
# TODO