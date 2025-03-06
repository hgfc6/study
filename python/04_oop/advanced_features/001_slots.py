# 定义完对象后我们可以任意给对象添加属性和方法，这就是动态语言的灵活性。
# 但是，如果我们想要限制对象可以添加的属性，可以使用__slots__来定义。
# __slots__定义了对象所能拥有的属性，一旦定义，则不能再添加新的属性。
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s = Student()
s.name = 'Alice'
s.age = 20
print(s.name, s.age)  # Alice 20

# 给s添加一个新属性：
# s.gender = 'female'  # 试图添加一个新属性gender # AttributeError: 'Student' object has no attribute 'gender' and no __dict__ for setting new attributes

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class PrimaryStudent(Student):
    pass
p = PrimaryStudent()
p.gender = 'female'
print(p.gender) # female

class JuniorStudent(Student):
    __slots__ = ('gender', 'grade')

    def describe(self):
        print('I am a junior student, my name is {}, my age is {}, my gender is {} and my grade is {}'.format(self.name, self.age, self.gender, self.grade))

j = JuniorStudent()
j.gender = 'male'
j.grade = 3
j.name = 'Bob'
j.age = 18
j.describe() # I am a junior student, my name is Bob, my age is 18, my gender is male and my grade is 3