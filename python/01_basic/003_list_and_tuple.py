# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
# 元组 tuple与列表类似，但是tuple一旦初始化就不能修改。

def test_tuple():
    print('------------------------------------')
    # 创建一个空元组
    my_tuple = ()
    # 创建一个非空元组
    my_tuple2 = (1, 2, 3)
    # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    my_tuple3 = (1,)
    # Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
    print(my_tuple3)  # 输出(1,)

    # 访问元组中的元素
    print(my_tuple2[0])  # 输出1
    print(my_tuple2[1])  # 输出2
    print(my_tuple2[2])  # 输出3
    # 元组长度
    print(len(my_tuple2))  # 输出3
    # 元组切片
    print(my_tuple2[1:3])  # 输出(2, 3)
    # 元组相加   # 元组不能相加
    # my_tuple3 = my_tuple2 + my_tuple
    # print(my_tuple3)  # 输出TypeError: can only concatenate tuple (not "int") to tuple
    # 元组元素修改
    # my_tuple2[0] = 4
    # print(my_tuple2)  # 输出TypeError: 'tuple' object does not support item assignment
    # 元组元素删除
    # del my_tuple2[1]
    # print(my_tuple2)  # 输出TypeError: 'tuple' object doesn't support item deletion

# 切片
def test_slice():
    print('------------------------------------')
    # 切片操作
    # 集合list
    # 语法：list[start:end:step]
    # start：起始索引，默认为0
    # end：结束索引，默认为列表长度
    # step：步长，默认为1
    # 负数索引：-1表示最后一个元素，-2表示倒数第二个元素，以此类推
    # 步长为负：表示逆序切片
    # 省略start：表示从头开始
    # 省略end：表示到末尾结束
    # 省略step：表示步长为1
    # 空切片：[:]表示复制整个列表
    # 复制列表：list[:]
    # 字符串切片：字符串[start:end:step]
    # 元组切片：元组[start:end:step]

    my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(my_list4[::2])  # 输出[1, 3, 5, 7, 9]
    print(my_list4[::-1])  # 输出[9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(my_list4[1:7:2])  # 输出[2, 4, 6]
    print(my_list4[1:-1:2])  # 输出[2, 4, 6, 8]

    my_tuple4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(my_tuple4[::2])  # 输出(1, 3, 5, 7, 9)
    print(my_tuple4[::-1])  # 输出(9, 8, 7, 6, 5, 4, 3, 2, 1)
    print(my_tuple4[1:7:2])  # 输出(2, 4, 6)
    print(my_tuple4[1:-1:2])  # 输出(2, 4, 6, 8)

    my_str4 = '123456789'
    print(my_str4[::2])  # 输出'13579'
    print(my_str4[::-1])  # 输出'987654321'
    print(my_str4[1:7:2])  # 输出'246'
    print(my_str4[1:-1:2])  # 输出'2468'
if __name__ =='__main__':
    # 创建一个空列表
    my_list = []
    # 创建一个非空列表
    my_list2 = [1, 2, 3]
    # 向列表中添加元素
    # 追加元素到末尾append
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    # 访问列表中的元素
    print(my_list[0])  # 输出1
    print(my_list[1])  # 输出2
    print(my_list[2])  # 输出3
    # 列表长度
    print(len(my_list))  # 输出3
    # 列表切片
    print(my_list[1:3])  # 输出[2, 3]
    # 列表相加
    my_list2 = [4, 5, 6]
    my_list3 = my_list + my_list2
    print(my_list3)  # 输出[1, 2, 3, 4, 5, 6]
    # 列表元素修改
    my_list[0] = 4
    print(my_list)  # 输出[4, 2, 3]
    # 列表删除指定索引处的元素 如果索引超出范围，会引发 IndexError
    del my_list[1]
    print(my_list)  # 输出[4, 3]

    # list常用方法
    # 1.count(x)：返回列表中元素x出现的次数
    print(my_list.count(3))  # 输出1
    # 2.index(x)：返回列表中第一次出现元素x的索引
    print(my_list.index(3))  # 输出1
    # 3.insert(i, x)：在索引i处插入元素x，其他元素后移
    my_list.insert(1, 5)
    print(my_list)  # 输出[4, 5, 3]
    # 4.pop(i)：删除并返回列表中索引i处的元素
    print(my_list.pop(1))  # 输出5
    print(my_list)  # 输出[4, 3]
    # 5.remove(x)：删除列表中第一个出现的元素x 如果值不在列表中，会引发 ValueError
    my_list.remove(3)
    print(my_list)  # 输出[4]
    # 6.reverse()：反转列表元素
    my_list = [4, 3]
    my_list.reverse()
    print(my_list)  # 输出[3, 4]
    # 7.sort()：对列表元素进行排序
    my_list.sort()
    print(my_list)  # 输出[3, 4]
    # 8.clear()：清空列表
    my_list.clear()
    print(my_list)  # 输出[]

    test_tuple()

    test_slice()

