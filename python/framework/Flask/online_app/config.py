import os

class Config:
    # SECRET_KEY 用于 session 签名和 CSRF 防护；生产环境必须从环境变量读取强随机值。
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cjh'

    # 默认使用 SQLite，便于本地学习；部署时可以通过 DATABASE_URL 切换数据库。
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'

    # 关闭对象变更追踪，减少不必要的内存开销。
    SQLALCHEMY_TRACK_MODIFICATIONS = False
