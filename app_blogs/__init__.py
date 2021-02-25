from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_moment import Moment

migrate = Migrate()
db = SQLAlchemy()
login = LoginManager()
login.login_view = 'logins'
moment = Moment()

def main_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    moment.init_app(app)

    # 这里是实例化蓝图
    from app_blogs.home_page import bp as home_bp
    app.register_blueprint(home_bp)

    from app_blogs.about import bp as about_bp
    app.register_blueprint(about_bp)


    from app_blogs.sign_in import bp as sign_bp
    app.register_blueprint(sign_bp)

    from app_blogs.cancellation import bp as can_bp
    app.register_blueprint(can_bp)

    from app_blogs.classification import bp as class_bp
    app.register_blueprint(class_bp)

    from app_blogs.artcle import bp as artcle_bp
    app.register_blueprint(artcle_bp)



    return app

from app_blogs import models