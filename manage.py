"""一，集成配置类
    二，sqlalchemy"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    # 调试模式
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/information12'
    # 数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app = Flask(__name__)

# 集成配置类
app.config.from_object(Config)
# 集成Sqlalchemy到flask
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run(debug=True)
