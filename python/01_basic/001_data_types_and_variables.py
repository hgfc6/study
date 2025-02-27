# 数据类型与变量

if __name__ == '__main__':
    # 整数类型
    a = 10
    print(a)
    print(type(a))

    # 浮点数类型
    b = 3.14
    print(b)
    print(type(b))

    # 字符串类型
    c = "hello, world"
    c2 = 'hello, world'  # 普通写法
    c3 = """hello, 
    
    world"""
    c4 = '''hello,\n world'''  # 多行写法
    c5 = r"hello, \n world"  # 原始字符串
    print(c, c2, c3, c4, c5)
    print(type(c))

    # 布尔类型
    d = True
    d2 = False
    d3 = d and d2  # 与
    d4 = d or d2  # 或
    d5 = not d2  # 非
    # d6 = d3 && d4  # 错误，不能使用 && 运算符
    # d7 = d3 || d4  # 错误，不能使用 || 运算符
    # d8 = !d2  # 错误，不能使用 ! 运算符
    print(d, d2, d3, d4, d5)
    print(type(d))

    # 空值类型
    e = None
    # e2 = null  # 错误，null 不是关键字
    # e2 = undefined  # 错误，undefined 不是关键字
    print(e)
    print(type(e))

    # 常量 常量是不能修改的变量，在程序运行期间保持不变的值 通常用全部大写的变量名表示常量
    PI = 3.141592653589793

    # 变量赋值用'='
    a = 20
    print(a)

    # 变量类型转换
    a = int(a)
    b = float(a)
    c = str(a)
    d = bool(a)
    e = None
    print(a, b, c, d, e)
    print(type(a), type(b), type(c), type(d), type(e))

    # 变量比较
    a = 10
    b = 20
    print(a == b) # False
    print(a != b) # True
    print(a  == 10) # True
    print(a  == "10") # False
    print(a  == True) # False
    print(a  == False) # False
    print(a is None) # False
    print(a  < b)  # True
    print(a  > b)  # False
    print(a  <= b)  # True
    print(a  >= b)  # False
    print(a is b)  # False
    # 在 Python 中，is 是一个比较运算符，用于判断两个对象是否为同一对象（即它们的内存地址是否相同）。它检查的是对象的身份，而不是对象的值。
    # == 是用来比较两个对象的值是否相等，而 is 是用来比较两个对象的身份是否相同。
    # 常用的方法是：
    # if variable is None:
    #     # 进行相应处理
    print(a is not b)  # True

    # 变量运算
    a = 10 + 20
    print(a)

    a = 10 - 20
    print(a)

    a = 10 * 20
    print(a)

    a = 10 / 20 # 除法运算结果为浮点数 0.5
    print(a)

    a = 10 // 20 # 除法运算结果为整数 0
    print(a)

    a = 10 % 20 # 取余运算 10
    print(a)

    a = 10 ** 3 # 幂运算  1000
    a22 = 10^3 # 异或运算 1010^0011=1001 9
    print(a, a22)

    # 变量命名规则
    # 1. 必须以字母或下划线开头
    # 2. 不能以数字开头
    # 3. 区分大小写
    # 4. 不能使用关键字
    # 5. 尽量简短，易于理解

    # 变量作用域
    # 1. 局部作用域：函数内部定义的变量，只在函数内有效
    # 2. 全局作用域：函数外部定义的变量，在整个程序内有效
    # 3. 内置作用域：系统预定义的变量，如：__name__、__main__
    # 变量命名建议
    # 1. 见名思意，变量名应该能够反映变量的含义
    # 2. 变量名尽量短，不要超过8个字符
    # 3. 变量名应该全部小写，多个单词用下划线连接
    # 4. 变量名应该有意义，不要使用拼音、缩写、数字代替
    # 5. 变量名应该有意义，不要使用特殊字符
    # 6. 变量名应该有意义，不要使用缩写
    # 7. 变量名应该有意义，不要使用无意义的变量名
    # 8. 变量名应该有意义，不要使用与系统关键字冲突的变量名
    # 9. 变量名应该有意义，不要使用与函数名冲突的变量名
