# dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 要牢记的第一条就是dict的key必须是不可变对象
# 第二条就是dict的key必须是可哈希的，即必须实现__hash__()方法，且返回的结果必须是整数。
# 第三条就是dict的key不能重复，如果重复，后面的值会覆盖前面的值。
# 第四条就是dict的key-value对是无序的。

# set的支持，set是一种无序的集合，可以用来存储一组不重复的元素。
# 要牢记的第一条就是set的元素必须是不可变对象。
# 第二条就是set的元素必须是可哈希的，即必须实现__hash__()方法，且返回的结果必须是整数。
# 第三条就是set的元素不能重复，如果重复，后面的元素会被自动忽略。
# 第四条就是set是无序的。

# 不可变对象
# 字符串、数字、元组都是不可变对象，因此可以作为dict的key。
# 列表、字典、集合都是可变对象，不能作为dict的key。
# 详细内容请参考：https://docs.python.org/zh-cn/3/glossary.html#term-immutable


if __name__ == '__main__':
    # 定义一个字典
    my_dict = {'apple': 1, 'banana': 2, 'orange': 3}
    print(my_dict)  # {'apple': 1, 'banana': 2, 'orange': 3}

    # 访问字典中的值
    print(my_dict['apple'])  # 1
    # 如果key不存在，dict就会报错
    # print(my_dict['grape'])  # KeyError: 'grape'
    # 要避免key不存在的错误，有两种办法，
    # 一是通过in判断key是否存在：
    if 'grape' in my_dict:
        print(my_dict['grape'])  # 输出不存在的key对应的值
    else:
        print('key not found')  # 输出提示信息

    # 也可以通过dict提供的get方法，如果key不存在，则返回None或自己指定的value：
    print(my_dict.get('grape'))  # None 注意：返回None的时候Python的交互环境不显示结果。
    print(my_dict.get('grape', 4))  # 4

    # 修改字典中的值
    my_dict['apple'] = 5
    print(my_dict)  # {'apple': 5, 'banana': 2, 'orange': 3}

    # 添加字典中的元素
    my_dict['grape'] = 4
    print(my_dict)  # {'apple': 5, 'banana': 2, 'orange': 3, 'grape': 4}

    # 删除字典中的元素 del或者dict.pop()
    # del my_dict['banana']
    my_dict.pop('banana')
    print(my_dict)  # {'apple': 5, 'orange': 3, 'grape': 4}
    # 如果删除的key不存在，dict.pop()会报错
    # my_dict.pop('banana')  # KeyError: 'banana'
    # del和dict.pop()都可以删除一个key-value对，但是返回值不同。
    # del不返回值, 更通用 除了字典，还可以用于删除列表中的元素、模块中的属性等
    # dict.pop()返回被删除的值。二者删除不存在的key都会报错，但是pop可以用第二个参数指定不存在时的返回值。

    # 遍历字典
    # 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
    for key in my_dict:
        print(key, my_dict[key])  # apple 5  banana 2  orange 3  grape 4

    # 遍历字典的key
    for key in my_dict.keys():
        print(key)  # apple  banana  orange  grape

    # 遍历字典的value
    for value in my_dict.values():
        print(value)  # 5  2  3  4

    # 遍历字典的key-value对
    for key, value in my_dict.items():
        print(key, value)  # apple 5  banana 2  orange 3  grape 4

    # 清空字典
    my_dict.clear()
    print(my_dict)  # {}


    print('-----------------------------------')
    # 定义一个集合
    my_set = {1, 2, 3, 3, 2, 1}
    print(my_set)  # {1, 2, 3}

    # 集合中的元素是无序的，因此输出结果可能与定义时的顺序不同。

    # 集合的操作
    # 并集
    print(my_set.union({4, 5, 6}))  # {1, 2, 3, 4, 5, 6}

    # 交集
    print(my_set.intersection({2, 3, 4}))  # {2, 3}

    # 差集
    print(my_set.difference({2, 3, 4}))  # {1}

    # 对称差集
    print(my_set.symmetric_difference({2, 3, 4}))  # {1, 4}