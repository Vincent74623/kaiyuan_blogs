from app_blogs import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app_blogs import login

# 这个是用来加载用户跟踪的
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# 用户模型
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(100),index=True,unique=True)
    email = db.Column(db.String(138),index=True,unique=True)
    password_hash = db.Column(db.String(168))

    # 这个用来以文章模型user_id关联的
    posts = db.relationship('Post',backref='us',lazy='dynamic')

    # 加密密码
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    # 解密密码
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

# 分类模型
class Fen(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40),index=True,unique=True)

    # 这个用来以文章模型fen_id关联的
    posts = db.relationship('Post',backref='fe',lazy='dynamic')

# 文章模型
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body_title = db.Column(db.String(60),index=True,unique=True)
    body_url = db.Column(db.String(250),index=True,unique=True)
    body = db.Column(db.Text)
    timeramp = db.Column(db.DateTime,index=True,default=datetime.utcnow)

    # User外键
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Fen外键
    fen_id = db.Column(db.Integer, db.ForeignKey('fen.id'))
