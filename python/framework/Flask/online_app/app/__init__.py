from flask import Flask
from config import Config
from .models import db
from .routes import login_manager

def create_app():
    # 应用工厂模式：把 app 的创建过程封装成函数，便于测试和多环境配置。
    app = Flask(__name__, template_folder='../templates/')

    # 从配置类加载 SECRET_KEY、数据库地址等配置。
    app.config.from_object(Config)

    # 初始化登录管理器，让 Flask-Login 接管登录状态。
    login_manager.init_app(app)

    # 初始化数据库扩展。这里没有直接绑定全局 app，方便应用工厂模式复用。
    db.init_app(app)

    # 注册蓝图，把 routes.py 中定义的一组路由挂载到应用上。
    from . import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        # 学习 Demo 中直接创建表；真实项目建议使用数据库迁移工具管理表结构。
        db.create_all()

    return app
