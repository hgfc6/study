from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# SQLAlchemy 扩展对象先创建，稍后在应用工厂里通过 init_app 绑定 Flask app。
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """用户表。UserMixin 提供 Flask-Login 需要的基础属性和方法。"""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # 永远不要把明文密码直接存进数据库，只保存不可逆的哈希值。
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # 登录时把用户输入的密码和数据库中的哈希值进行校验。
        return check_password_hash(self.password_hash, password)

class Document(db.Model):
    """文档表。每篇文档通过 user_id 关联到创建它的用户。"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # relationship 让代码可以通过 doc.user 访问作者，也可以通过 user.documents 访问文档列表。
    user = db.relationship('User', backref=db.backref('documents', lazy=True))
