# 字符串编码

# 字符串编码是指将字符串转换为机器可以识别的二进制数据，以便计算机可以处理和存储。

if __name__ == '__main__':
    # 字符串编码
    s = 'Hello, world!'
    print(s)  # Hello, world!
    # 字符串编/解码方式
    print(s.encode('ascii'), b'Hello, world!'.decode('ascii'))  # b'Hello, world!' Hello, world!
    # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
    print("中国".encode('utf-8'), b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('utf-8'))  # b'\xe4\xb8\xad\xe5\x9b\xbd' 中国
    # 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
    print(b'\xe4\xb8\xad\xe5\x9b\xbd\xff'.decode('utf-8', errors='ignore'))  # 中国

    # 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
    print(ord('A'), ord('中'))  # 65 20013
    print(chr(65), chr(20013))  # A 中

    # Python对bytes类型的数据用带b前缀的单引号或双引号表示
    b = b'Hello, world!'
    print(b)  # b'Hello, world!'

    # len()函数计算的是字节数，而非字符数：
    print(len('ABC'))  # 3
    print(len('中文'))  # 6
    print(len(b'ABC'))  # 3
    print(len('中文'.encode('utf-8')))  # 6

    # 格式化 %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数
    # 三种方式 % format f_string
    # %
    print('Hello, %s, 成绩提升了 %.1f%%' % ('小明', 17.56789))  # Hello, 小明, 成绩提升了 17.6%

    # str.format():占位符以{}包围，数字对应实际值在位置参数中，关键字对应实际值在字典参数中。
    print('Hello, {0}, 成绩提升了 {1}%'.format('小明', 17.56789))  # Hello, 小明, 成绩提升了 17.56789%
    print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.56789))  # Hello, 小明, 成绩提升了 17.57%

    # f_string 使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换
    name = '小明'
    score = 17.56789
    print(f'Hello, {name}, 成绩提升了 {score:.2f}%')  # Hello, 小明, 成绩提升了 17.57%
    # %%表示一个普通的%字符
    # 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
