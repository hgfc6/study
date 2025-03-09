# 文件读写
import logging

# 写入文件
try:
    f = open("file.txt", "w")
    f.write("Hello, world!")
except IOError:
    logging.error("File operation failed")
finally:
    if f:
        f.close()

# 读取文件
try:
    f = open("file.txt", "r")
    content = f.read()
    print(content)
except IOError:
    logging.error("File operation failed")
finally:
    if f:
        f.close()

# 每次都这么写finally很麻烦，所以，Python引入了with语句来自动帮我们调用close()方法
with open("file.txt", "r") as f:
    content = f.read()
    print('with open', content)
# read()一次读文件全部内容，如果文件很大，内存可能爆掉，所以，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 或者使用readline()每次读取一行内容/readlines()一次读取所有行，返回一个列表。
with open("file.txt", "r") as f:
    while True:
        content = f.read(1024)
        if not content:
            break
        print('read', content)
with open("file.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print('readline', line.strip())
with open("file.txt", "r") as f:
    for line in f.readlines():
        print('readlines', line.strip())
# 写入文件时，如果文件不存在，会自动创建，如果文件存在，会覆盖原文件。
# 读写文件时，务必注意异常处理，否则，可能会导致程序崩溃或者数据丢失。


# file-like object
# 除了文件，Python还支持其他对象作为文件，比如内存中的字节流，网络流，自定义流等。
# 这些对象都实现了read()方法，可以用来读取数据，还可以实现write()方法，用来写入数据。
# 所以，我们可以把这些对象看作文件，然后用文件操作函数来操作它们。
# 例如
# 可以用BytesIO()创建一个内存中的字节流，然后用文件操作函数来操作它。
# 如果想操作内存中的字符串，可以用StringIO()创建一个内存中的字符串流。
from io import BytesIO

# 写入内存中的字节流
try:
    f = BytesIO()
    f.write(b"Hello, world!")
    content = f.getvalue()
    print(content)
except IOError:
    logging.error("File operation failed")
finally:
    if f:
        f.close()

# 读取内存中的字节流
try:
    f = BytesIO(b"Hello, world!")
    content = f.read()
    print(content)
except IOError:
    logging.error("File operation failed")
finally:
    if f:
        f.close()



# 二进制内容
# 如果文件是二进制文件，比如图片、视频等，则需要用二进制模式打开文件，用b前缀表示。
# 例如，读取图片文件时，用rb模式打开文件，wb模式写入文件，用read()方法读取图片内容，用write()方法写入图片内容。
# 所有模式请参考Python官方文档。https://docs.python.org/3/library/functions.html#open
# with open("image.jpg", "rb") as f:
#     content = f.read()
#     print(content)


# 字符编码
# 默认情况下，open()函数以文本模式打开文件，读取和写入的都是Unicode字符串。
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# with open("gbk.txt", "r", encoding="gbk") as f:
#     content = f.read()
#     print(content)