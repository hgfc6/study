# 循环

if __name__ == '__main__':
    # for 循环
    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
    # for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句

    # 如果要计算1-100的整数之和，从1写到100有点困难，
    # 幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
    for e in range(5):
        print(e)

    # while 循环
    i = 1
    while i <= 10:
        print(i)
        i += 1


    # break 语句 跳出循环
    i = 1
    while i <= 10:
        if i == 5:
            break
        print(i)
        i += 1

    # continue 语句 跳过当前循环，直接开始下一轮循环
    i = 1
    while i <= 10:
        if i == 5:
            i += 1
            continue
        print(i)
        i += 1
