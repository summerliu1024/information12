"""一，集成配置类
    二，sqlalchemy
    三，集成redis
    """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis


class Config(object):
    # 调试模式
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/information12'
    # 数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis ip和端口配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"


app = Flask(__name__)

# 集成配置类
app.config.from_object(Config)
# 集成Sqlalchemy到flask
db = SQLAlchemy(app)
# 连接redis
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route('/')
def index():
    redis_store.set("name", "summer")
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run(debug=True)
