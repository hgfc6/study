from flask import Flask
from config import Config
from .models import db
from .routes import login_manager

def create_app():
    app = Flask(__name__, template_folder='../templates/')
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    with app.app_context():
        db.create_all()

    return app