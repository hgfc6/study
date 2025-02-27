# 函数参数

# >>>>>>>>>位置参数
def my_func(a, b, c):
    print('a=%s, b=%s, c=%s' % (a, b, c))
    print('a={0}, b={1}, c={2}'.format(a, b, c))
    print(f'a={a}, b={b}, c={c}')
# 位置参数顺序必须与函数定义的顺序一致





# >>>>>>>>>默认参数
def my_func2(a, b, c=3, d=4): # c d 给了就用给的，没给就用默认值
    print('a=%s, b=%s, c=%s, d=%s' % (a, b, c, d))
    print('a={0}, b={1}, c={2}, d={3}'.format(a, b, c, d))
    print(f'a={a}, b={b}, c={c}, d={d}')

# 设置默认参数时，有几点要注意：
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 如果默认参数在前，必选参数在后，那么在调用函数时，解释器将无法明确区分哪些值是为默认参数提供的，哪些值是为必选参数提供的。这会导致参数赋值的混乱。
# 二是如何设置默认参数。
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
# 》》注意避坑《《
def my_append(L=[]):
    L.append('END')
    return L
# 当传入值时没问题
print(my_append([1, 2, 3])) # [1, 2, 3, 'END']
print(my_append(['x', 'y', 'z']))  # ['x', 'y', 'z', 'END']
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#  》》特别注意《《
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
print(my_append()) # ['END']
print(my_append()) # ['END', 'END']
print(my_append()) # ['END', 'END', 'END']
# 可以这样改
def my_append2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
# 这样每次调用函数时，都重新生成一个新的空列表，这样就不会有问题了。
print(my_append2()) # ['END']
print(my_append2()) # ['END']





# >>>>>>>>>可变参数
def my_add(a, b, *args):
    sum = 0
    for arg in args:
        sum += arg
    return a + b + sum
print(my_add(1, 2)) # 3
print(my_add(1, 2, 3)) # 6
print(my_add(1, 2, 3, 4)) # 10
print(my_add(1, 2, 3, 4, 5)) # 15






# >>>>>>>>>关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
# 关键字参数有什么用？它可以扩展函数的功能。比如，在my_func3函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
def my_func3(name, age, **kwargs):
    print('name=%s, age=%s kw=%s' % (name, age, kwargs))

my_func3('Alice', 25, city='Beijing', job='Engineer')
# 输出：name=Alice, age=25 kw={'city': 'Beijing', 'job': 'Engineer'}
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
my_dict = {'city': 'Beijing', 'job': 'Engineer'}
my_func3('Bob', 30, **my_dict)
# 输出：name=Bob, age=30 kw={'city': 'Beijing', 'job': 'Engineer'}
# 注意：my_func3得到的时my_dict的拷贝，对my_dict的改动不会影响到函数的行为, 函数内的my_dict是局部变量，外部的my_dict不会受到影响。






# >>>>>>>>>命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收指定名字的的kv作为关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 命名关键字参数必须填，不填会报错。
def person(name, age, *, city, job):
    print('name:', name, 'age:', age, 'city:', city, 'job:', job)

person('Jack', 24, city='Beijing', job='Engineer')
# 输出：name: Jack age: 24 city: Beijing job: Engineer

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print('name:', name, 'age:', age, 'args:', args, 'city:', city, 'job:', job)

person2('Mike', 23, 'hello', 'world', city='Shanghai', job='Doctor')
# 输出：name: Mike age: 23 args: ('hello', 'world') city: Shanghai job: Doctor

# 命名关键字参数可以有缺省值，从而简化调用：

def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
# 由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person3('Tom', 22, job='Teacher') # Tom 22 Beijing Teacher





# >>>>>>>>>组合参数
# 以上参数组合使用，可以组合使用，但要注意顺序：
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。

if __name__ == '__main__':
    # 位置参数
    my_func(1, 2, 3) # a=1, b=2, c=3


    # 默认参数
    my_func2(1, 2) # a=1, b=2, c=3, d=4
    my_func2(1, 2, c=5) # a=1, b=2, c=5, d=4
    my_func2(1, 2, d=6) # a=1, b=2, c=3, d=6


    # 可变参数
    print(my_add(1, 2)) # 3
    print(my_add(1,2,3,4)) # 10
    # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去, 这种写法相当有用，而且很常见
    print(my_add(1, 2, *[3, 4])) # 10
    print(my_add(1, 2, *(3, 4, 5))) # 15


    # 关键字参数
    my_func3('Alice', 25, city='Beijing', job='Engineer') # name=Alice, age=25 kw={'city': 'Beijing', 'job': 'Engineer'}
    my_func3('Alice', 25) # name=Alice, age=25 kw={}

    # 命名关键字参数，必须传入关键字参数名，否则会报错
    person('Jack', 24, city='Beijing', job='Engineer') # name: Jack age: 24 city: Beijing job: Engineer
    # person('Mike', 23) # TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
    # person('Mike', 23, city='Shanghai') # TypeError: person() missing 1 required keyword-only argument: 'job'
    person2('Mike', 23, 'hello', 'world', city='Shanghai', job='Doctor') # name: Mike age: 23 args: ('hello', 'world') city: Shanghai job: Doctor