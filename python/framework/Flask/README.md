`Flask 是一个用 Python 编写的轻量级 Web 应用框架。
Flask 基于 WSGI（Web Server Gateway Interface）和 Jinja2 模板引擎，旨在帮助开发者快速、简便地创建 Web 应用。`

# 安装
```
pip install Flask # 安装
pip show Flask # 查看 Flask 版本
```
# 基本概念

### 路由（Routing）

路由是指将客户端请求的 URL 与服务器端的具体函数绑定（映射）的过程。
```python
from flask import Flask

app = Flask(__name__)

@app.route('/') # 根路径
def home():
    return 'Welcome to the Home Page!'

@app.route('/about') # 关于页面
def about():
    return 'This is the About Page.'
```

### 视图函数（View Function）

视图函数是指接受客户端请求并返回响应的函数。
```python
@app.route('/greet/<name>') # 函数greet就是视图函数
def greet(name):
    return f'Hello, {name}!'
```

### 请求对象（Request Object）

请求对象是 Flask 中用于封装客户端请求信息的对象。Flask 提供了 request 对象来访问这些信息。
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    return f'Hello, {username}!'
```

### 响应对象（Response Object）

响应对象是 Flask 中用于封装服务器响应信息的对象。响应对象包含了发送给客户端的响应信息，包括状态码、响应头和响应体。Flask 默认会将字符串、HTML 直接作为响应体。
```python
from flask import make_response

@app.route('/custom_response')
def custom_response():
    response = make_response('This is a custom response!')
    response.headers['X-Custom-Header'] = 'Value'
    return response
```
### 模板（Templates）

模板是指服务器端返回给客户端的 HTML 页面，可以包含动态内容。
```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# hello.html 模板文件
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Hello, {{ name }}!</title>
# </head>
# <body>
#     <h1>Hello, {{ name }}!</h1>
# </body>
# </html>
```

### 静态文件（Static Files）

静态文件是指服务器端返回给客户端的非 HTML 文件，如 CSS、JavaScript、图片等。
```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
<!--静态文件目录：将静态文件放在 static 文件夹中，Flask 会自动提供服务。-->
```

### 应用工厂（Application Factory）

应用工厂是一个 Python 函数，用于创建和配置 Flask 应用实例。这种方法允许你创建多个应用实例，或者在不同配置下初始化应用。
```python
from flask import Flask
# create_app 函数创建一个 Flask 应用实例，并从配置对象中加载配置。
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    from . import routes
    app.register_blueprint(routes.bp)

    return app
```

### 配置对象

配置对象用于设置应用的各种配置选项，如数据库连接字符串、调试模式等。可以通过直接设置或加载配置文件来配置 Flask 应用。
```yaml
class Config:
    DEBUG = True
    SECRET_KEY = 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mydatabase.db'
#app.config.from_object(Config)：将 Config 类中的配置项加载到应用配置中。
```
### 蓝图（Blueprint）

蓝图是 Flask 中用于组织应用的模块化方法。它允许你将相关的视图函数、模板和静态文件组织在一起，并且可以在多个应用中重用。
```python
from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return 'Home Page'
```
```python
#注册蓝图 注册蓝图 (app/__init__.py)
from flask import Flask
from .routes import bp as main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
```

### 应用上下文（Application Context）

应用上下文是指 Flask 应用运行时期间的上下文，包括配置、请求上下文、会话、模板上下文等。

### 扩展（Extensions）

扩展是指 Flask 应用的插件，可以扩展应用的功能。
Flask 有许多扩展，可以添加额外的功能，如数据库集成、表单验证、用户认证等。这些扩展提供了更高级的功能和第三方集成。
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app) # SQLAlchemy：用于数据库集成的扩展。
```
### 会话（Sessions）

Flask 使用客户端会话来存储用户信息，以便在用户浏览应用时记住他们的状态。会话数据存储在客户端的 cookie 中，并在服务器端进行签名和加密。
```python
from flask import session

# 自动生成的密钥
app.secret_key = 'your_secret_key_here'

@app.route('/set_session/<username>')
def set_session(username):
    session['username'] = username
    return f'Session set for {username}'

@app.route('/get_session')
def get_session():
    username = session.get('username')
    return f'Hello, {username}!' if username else 'No session data'
# session 对象用于存取会话数据。
# 你可以使用 Python 内置的 secrets 模块生成一个强随机性的密钥。
# python3 -c 'import secrets; print(secrets.token_hex())'
```
### 错误处理（Error Handling）

错误处理是指 Flask 应用在处理请求过程中发生的错误，包括 404 错误、500 错误等。

```python
@app.errorhandler(404)
def page_not_found(e):
    return 'Page not found', 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500
```