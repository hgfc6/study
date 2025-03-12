# 使用指南
## 1. 安装
```
pip install django
```
## 2. 创建项目
```
django-admin startproject project_name
```
项目目录各文件说明：
```
project_name/ # 项目的容器。
    manage.py  # 项目管理文件， 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
    project_name/  # 项目目录
        __init__.py  # 一个空文件，告诉 Python 该目录是一个 Python 包。
        asgi.py  #  一个 ASGI 兼容的 Web 服务器的入口
        settings.py  # 项目设置文件
        urls.py  # 项目路由文件, 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
        wsgi.py  #  一个 WSGI 兼容的 Web 服务器的入口
        # 其他可能存在的目录或文件：
        migrations/  #  Django 数据库迁移文件目录
        tests/  #  Django 项目测试文件目录
        static/  #  静态文件目录
        templates/  #  模板文件目录
```
## 3. 创建应用
```
python manage.py startapp app_name
```
## 4. 运行项目
```
python manage.py runserver 0.0.0.0:8888
```
## 5. 访问项目
```
http://localhost:8888/
```

# 模板
作用：渲染 HTML 页面，配合views.py实现动态页面。
配置模板路径：在项目的settings.py文件中设置：
```
TEMPLATES = [
    {
        ...,
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...,
    },
]
```

模板语法参考 [Django 模板语言](https://docs.djangoproject.com/zh-hans/3.2/topics/templates/)

# 模型
作用：存储和管理数据，配合views.py实现数据交互。Django 对各种数据库提供了很好的支持，包括：PostgreSQL、MySQL、SQLite、Oracle。
配置DATABASES配置项：在项目的settings.py文件中设置：
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'your_database_host',
        'PORT': 'your_database_port',
    },
    ...
}
```
```python
import sqlite3
from pathlib import Path
sqlite3.connect(Path(__file__).parent / 'db.sqlite3')
```
### 创建 APP
Django 规定，如果要使用模型，必须要创建一个 app。我们使用以下命令在项目容器目录下创建一个 TestModel 的 app
```shell
python manage.py startapp TestModel
```



# 视图
作用：处理用户请求，返回响应。

# 路由
作用：将请求映射到视图，实现请求分发。

# 表单
作用：收集用户输入，验证输入，处理表单提交。

# 序列化器
作用：将模型实例转换为可用于网络传输的格式，如 JSON。

# 管理器
作用：提供模型管理的界面，如增删改查。

# 视图集
作用：将多个视图组合成一个视图，实现复用。

# 过滤器
作用：对模型实例进行过滤，实现数据筛选。

# 信号
作用：在模型实例发生特定事件时触发信号，执行相应的操作。

# 装饰器
作用：为视图函数添加额外的功能，如缓存、权限控制等。

# 缓存
作用：缓存视图函数的返回结果，提高响应速度。

# 权限控制
作用：限制用户对特定视图的访问权限。

# 国际化 
作用：支持多语言，实现多语言翻译。

# 静态文件
作用：提供静态文件，如图片、CSS、JavaScript 文件。

# 日志
作用：记录用户请求、错误信息等。

# 定时任务
作用：在指定时间执行任务，如清理缓存、发送邮件等。

# 部署
作用：将项目部署到服务器上，实现网站的上线。

