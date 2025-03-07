# 继承
# 继承是面向对象编程的一个重要概念，它允许创建新的类，从现有类继承属性和方法，并添加或修改属性和方法。
class Animal(object):
    def run(self):
        print("Animal is running.")


class Dog(Animal):
    pass


# 继承有什么好处？最大的好处是子类获得了父类的全部功能。
dog = Dog()
dog.run()  # Animal is running.


# <span id="dt">多态</span>
# 多态是指一个方法在不同的对象中有不同的表现形式。
# 多态的好处是代码的可读性和可维护性都得到提高。
# 子类的同名方法会覆盖主类的同名方法
class Dog(Animal):
    def run(self):
        print("Dog is running.")


class Cat(Animal):
    def run(self):
        print("Cat is running.")


Dog().run()  # Dog is running.
Cat().run()  # Cat is running.

# 判断是不是某一个类型的子类，可以用 isinstance() 函数。
print(isinstance(dog, Animal))  # True

# 多态符合了设计lipsis的原则，即“开闭原则”，即对扩展开放，对修改封闭。
# 五大设计原则
# 1. 单一职责原则（Single Responsibility Principle，SRP）
# 》》》一个类只负责一项职责，其它的功能都由该类来完成。
# 2. 开闭原则（Open-Closed Principle，OCP）
# 》》》软件实体应该对扩展开放，对修改封闭。
# 3. 依赖倒置原则（Dependency Inversion Principle，DIP）
# 》》》高层模块不应该依赖低层模块，两者都应该依赖其抽象。
# 4. 接口隔离原则（Interface Segregation Principle，ISP）
# 》》》使用多个专门的接口，而不使用单一的总接口。
# 5. 里氏替换原则（Liskov Substitution Principle，LSP）
# 》》》所有引用基类（父类）的地方必须能透明地使用其子类的对象。


# 静态语言 VS 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
def run_twice(animal):
    animal.run()
    animal.run()

class Bird(object):
    def run(self):
        print("Bird is flying.")

run_twice(Bird())  # Bird is flying. Bird is flying.
# 鸭子类型
# 鸭子类型是指，只要一个对象看起来像鸭子，就可以把它当做鸭子来用。
# 例如，我们只需要传入一个run()方法的对象，就可以把它当做一个Animal来用。
