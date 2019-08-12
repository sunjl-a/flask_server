from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel


# flask实例化，生成对象app
app = Flask(__name__)
# 本地化，将网页内容改为中文显示
babel = Babel(app)
URI = 'mysql+pymysql://name:passwoed@1XX.2XX.3XX.4XX:8080/automation?charset=utf8'
app.config.update(
    SQLALCHEMY_DATABASE_URI=URI,
    BABEL_DEFAULT_LOCALE='zh_CN',
    SECRET_KEY='123qweasd',
    JSON_AS_ASCII=False
)
db = SQLAlchemy(app)

admin = Admin(app, name='任务调度中心', template_mode='bootstrap3')

