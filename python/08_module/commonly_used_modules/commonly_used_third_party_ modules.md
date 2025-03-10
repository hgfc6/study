以下是 Python 中一些常用的第三方模块：
## Pillow
Pillow 是一个 Python 图像处理库，可以用来处理图像、视频、图形、字体等。

安装：
```
pip install Pillow
```
操作图像：
```python
from PIL import Image
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('test.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')
```


## requests
requests 是一个 HTTP 库，可以用来发送 HTTP 请求。
安装：
```
pip install requests
```
发送 GET 请求：
```python
import requests

response = requests.get('https://www.example.com')
print(response.status_code)
print(response.content)
```

发送 POST 请求：
```python
import requests

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.status_code)
print(response.content)
```

## chardet
chardet 是一个字符编码检测库，可以用来检测网页、文本、二进制文件的编码。
安装：
```
pip install chardet
```
检测网页编码：
```python
import requests
from chardet.universaldetector import UniversalDetector

def detect_encoding(url):
    detector = UniversalDetector()
    response = requests.get(url)
    for line in response.iter_lines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']

url = 'https://www.example.com'
encoding = detect_encoding(url)
print(encoding)
```

## psutil
psutil 是一个跨平台库，可以用来获取系统信息、进程信息、内存信息等。psutil = process and system utilities
安装：
```
pip install psutil
```
获取系统信息：
```python
import psutil

def get_system_info():
    # 获取系统信息
    system_info = {}
    system_info['platform'] = psutil.platform()
    system_info['system'] = psutil.system()
    system_info['node'] = psutil.node()
    system_info['release'] = psutil.release()
    system_info['version'] = psutil.version()
    system_info['machine'] = psutil.machine()
    return system_info

system_info = get_system_info()
print(system_info)
```

获取进程信息：
```python
import psutil

def get_process_info():
    # 获取进程信息
    process_info = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            process_info.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_info

process_info = get_process_info()
print(process_info)
```

获取内存信息：
```python
import psutil

def get_memory_info():
    # 获取内存信息
    memory_info = {}
    memory_info['total'] = psutil.virtual_memory().total
    memory_info['available'] = psutil.virtual_memory().available
    memory_info['used'] = psutil.virtual_memory().used
    memory_info['percent'] = psutil.virtual_memory().percent
    return memory_info

memory_info = get_memory_info()
print(memory_info)
```

## BeautifulSoup
BeautifulSoup 是一个 Python 库，可以用来解析 HTML 文档。
安装：
```
pip install beautifulsoup4
```
解析 HTML 文档：
```python
from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 解析标题
    title = soup.title.string
    # 解析链接
    links = [link.get('href') for link in soup.find_all('a')]
    # 解析图片
    images = [image.get('src') for image in soup.find_all('img')]
    return title, links, images

html = '<html><head><title>Example</title></head><body><h1>Hello, world!</h1><a href="https://www.example.com">Link</a><img src="https://www.example.com/image.jpg"></body></html>'
title, links, images = parse_html(html)
print(title)
print(links)
print(images)
```

## PyMySQL
PyMySQL 是一个 Python 库，可以用来操作 MySQL 数据库。
安装：
```
pip install PyMySQL
```
连接数据库：
```python
import pymysql

def connect_mysql():
    # 连接数据库
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='password',
        database='database',
        charset='utf8mb4'
    )
    return conn

conn = connect_mysql()
```
执行 SQL 语句：
```python
import pymysql

def execute_sql(conn, sql):
    # 执行 SQL 语句
    with conn.cursor() as cursor:
        cursor.execute(sql)
        conn.commit()

    return cursor.rowcount

sql = 'INSERT INTO table (column1, column2) VALUES (%s, %s)'
params = ('value1', 'value2')
rowcount = execute_sql(conn, sql, params)
print(rowcount)
```

## PyYAML
PyYAML 是一个 Python 库，可以用来解析 YAML 格式的配置文件。

## 其他常用第三方模块
- Flask：一个轻量级的 Python Web 框架，可以用来开发 Web 应用。
- Django：一个 Python Web 框架，可以用来开发复杂的 Web 应用。
- Scrapy：一个 Python 爬虫框架，可以用来抓取网页数据。
- Matplotlib：一个 Python 绘图库，可以用来创建图表。
- TensorFlow：一个开源的机器学习框架，可以用来构建深度学习模型。
- Keras：一个高级的神经网络 API，可以用来构建深度学习模型。
- PyTorch：一个开源的深度学习框架，可以用来构建深度学习模型。
- NLTK：一个 Python 自然语言处理库，可以用来处理文本数据。
- NumPy：一个 Python 科学计算库，可以用来处理数组和矩阵。
- Pandas：一个 Python 数据分析库，可以用来处理数据集。
- Scipy：一个 Python 科学计算库，可以用来处理信号、图像、优化等。
- Scikit-learn：一个 Python 机器学习库，可以用来构建机器学习模型。
- Statsmodels：一个 Python 统计学库，可以用来进行统计分析。
- Bokeh：一个 Python 可视化库，可以用来创建交互式图表。
- Pytest：一个 Python 测试框架，可以用来编写和运行测试用例。
- Selenium：一个用于 Web 自动化测试的 Python 库，可以用来编写自动化测试用例。
