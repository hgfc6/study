# 单元测试
# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def tearDown(self):
        print('tearDown')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
# 常用方法
# assertEqual()方法用于判断两个对象是否相等，如果不相等，则抛出AssertionError异常。
# assertTrue()方法用于判断一个对象是否为True，如果不是True，则抛出AssertionError异常。
# assertFalse()方法用于判断一个对象是否为False，如果不是False，则抛出AssertionError异常。
# assertRaises()方法用于测试一个函数是否抛出指定类型的异常，如果函数没有抛出指定类型的异常，则抛出AssertionError异常。
# assertIn()方法用于判断一个对象是否在一个序列中，如果不在，则抛出AssertionError异常。
# assertNotIn()方法用于判断一个对象是否不在一个序列中，如果在，则抛出AssertionError异常。
# assertIs()方法用于判断两个对象是否是同一个对象，如果不是，则抛出AssertionError异常。
# assertIsNot()方法用于判断两个对象是否不是同一个对象，如果是，则抛出AssertionError异常。
# assertIsNone()方法用于判断一个对象是否为None，如果不是None，则抛出AssertionError异常。
# assertIsNotNone()方法用于判断一个对象是否不为None，如果为None，则抛出AssertionError异常。
# assertAlmostEqual()方法用于判断两个浮点数是否相等，如果不相等，则抛出AssertionError异常。
# assertNotAlmostEqual()方法用于判断两个浮点数是否不相等，如果相等，则抛出AssertionError异常。
# assertGreater()方法用于判断一个对象是否大于另一个对象，如果不大于，则抛出AssertionError异常。
# assertGreaterEqual()方法用于判断一个对象是否大于等于另一个对象，如果不大于等于，则抛出AssertionError异常。
# assertLess()方法用于判断一个对象是否小于另一个对象，如果不小于，则抛出AssertionError异常。
# assertLessEqual()方法用于判断一个对象是否小于等于另一个对象，如果不小于等于，则抛出AssertionError异常。
# assertRegex()方法用于判断一个字符串是否匹配一个正则表达式，如果不匹配，则抛出AssertionError异常。
# assertNotRegex()方法用于判断一个字符串是否不匹配一个正则表达式，如果匹配，则抛出AssertionError异常。
# assertCountEqual()方法用于判断两个序列中的元素是否相同，但顺序可以不同，如果不相同，则抛出AssertionError异常。
# assertMultilineEqual()方法用于判断两个字符串是否相等，并且换行符也相同，如果不相等，则抛出AssertionError异常。
# ......
# setUp()方法在每个测试方法执行之前被调用，可以用于初始化测试环境。
# tearDown()方法在每个测试方法执行之后被调用，可以用于清理测试环境。

# 运行单元测试
# 最简单的运行方式是在mydict_test.py的最后加上两行代码
# if __name__ == '__main__':
#     unittest.main()
# 然后在命令行中运行python mydict_test.py即可运行单元测试。
# 另一种方法是在命令行通过参数-m unittest直接运行单元测试，(推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试)
# 例如：
# python -m unittest mydict_test.py

if __name__ == '__main__':
    unittest.main()