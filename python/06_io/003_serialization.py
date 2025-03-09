# 序列化
# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
# 反之，把变量内容从序列化的对象重新读到内存里称之为反序列化，在Python中叫unpickling
import pickle

# 序列化对象
data = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
serialized_data = pickle.dumps(data)
print(serialized_data) # b'\x80\x04\x95-\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x05Alice\x94\x8c\x03age\x94K\x19\x8c\x04city\x94\x8c\x07Beijing\x94u.'

# 反序列化对象
deserialized_data = pickle.loads(serialized_data)
print(deserialized_data) # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。



# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON，
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

import json

# 序列化对象
data = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
serialized_data = json.dumps(data)
print(serialized_data) # {"name": "Alice", "age": 25, "city": "Beijing"}

# 反序列化对象
deserialized_data = json.loads(serialized_data)
print(deserialized_data) # {'name': 'Alice', 'age': 25, 'city': 'Beijing'}

# 注意，JSON的字符串和Python的字典是一样的，所以可以直接用loads()方法反序列化。
# 常用方法：
# dumps()方法用于序列化，它返回一个JSON格式的字符串。
# loads()方法用于反序列化，它接受一个JSON格式的字符串，并返回一个Python对象。
# dump()方法用于将对象序列化到一个文件，比如json.dump()。
# load()方法用于从文件反序列化，比如json.load()。

# 自定义类序列化
# 自定义类直接使用pickle序列化是不行的，因为pickle只能序列化基本类型，不能序列化自定义类。
# 要想序列化自定义类要看dumps()方法的第二个参数default，它是一个函数，用于指定如何序列化自定义类。
# 这个函数的输入是自定义类的实例，输出是要序列化的对象。

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

def serialize_person(person):
    return {'name': person.name, 'age': person.age, 'city': person.city}

# 序列化对象
person = Person('Alice', 25, 'Beijing')
serialized_data = json.dumps(person, default=serialize_person)
print(serialized_data) # {"name": "Alice", "age": 25, "city": "Beijing"}
# 反序列化对象
deserialized_data = json.loads(serialized_data, object_hook=lambda d: Person(d['name'], d['age'], d['city']))
print(deserialized_data) # <__main__.Person object at 0x7f9d5d9d9a90>

