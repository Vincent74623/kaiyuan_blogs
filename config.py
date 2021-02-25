import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    POSTS_PER_PAGE = 2
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'dataa.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ffsfsfsafsafghgfvchjuthgrfeacdscasf-sdf-aasfas-fasdf-asfs-fa'