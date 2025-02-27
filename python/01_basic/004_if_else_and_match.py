# 条件判断

if __name__ == '__main__':
    # 条件判断
    # if 条件表达式:(注意if后面没有括号)
    #     语句块
    # elif 条件表达式:
    #     语句块
    # else:
    #     语句块

    # 示例1：判断一个数是否为偶数
    num = 10
    if num % 2 == 0:
        print(num, "是偶数")
    else:
        print(num, "是奇数")

    # 示例2：判断一个数是否为正数、负数或零
    num = 0
    if num > 0:
        print(num, "是正数")
    elif num < 0:
        print(num, "是负数")
    else:
        print(num, "是零")

    # 模式匹配
    # match 表达式:
    #     case 模式1:
    #         语句块
    #     case 模式2:
    #         语句块
    #     ...
    #     case 模式n:
    #         语句块
    #     case _:
    #         语句块

    # 示例3：判断一个数是否为1、2、3、4、5、6、7、8、9、10
    num = 7
    match num:
        case 1:  # 简单匹配
            print(num, "是1")
        case x if x < 5:
            print(x, '是2-5之间的数字')
        case 5 | 6 | 7 | 8:  # 匹配多个值
            print(num, "是5-8之间的数字")
        case _:  # _表示匹配到其他任何情况
            print(num, "> 8")

    # 匹配列表
    # match语句还可以匹配列表，功能非常强大。
    # 我们假设用户输入了一个命令，用args = ['gcc', 'hello.c']存储，下面的代码演示了如何用match匹配来解析这个列表：

    args = ['gcc', 'hello.c', 'world.c']
    # args = ['clean']
    # args = ['gcc']

    match args:
        # 表示列表仅有 gcc 一个字符串，没有指定文件名，报错；
        case ['gcc']:
            print('gcc: missing source file(s).')
        # 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，
        # 后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
        case ['gcc', file1, *files]:
            print('gcc compile: ' + file1 + ', ' + ', '.join(files))
        # 仅出现clean:
        case ['clean']:
            print('clean')
        case _:
            print('invalid command.')
