"""一，集成配置类
    二，sqlalchemy
    三，集成redis
    四，集成csrfprotect
    五，集成flask-session
    """

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session


class Config(object):
    SECRET_KEY='djfdshlfkhsdakfhasdklfhkpas;d'
    # 调试模式
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/information12'
    # 数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis ip和端口配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    # flask-session的配置信息
    SESSION_TYPE = 'redis'
    # 指定存储session的存储对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置session签名
    SESSION_USE_SIGNER = True
    # 设置session永久保存与否
    SESSION_PERMANENT = False
    # 设置session的保存时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)

# 集成配置类
app.config.from_object(Config)
# 集成Sqlalchemy到flask
db = SQLAlchemy(app)
# 连接redis
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# CSRFPROTECT保护
CSRFProtect(app)

# 集成flask-session
# 说明 flask中的session是保存用户数据的容器（上下文），而flask-session是指定session保存的路径
Session(app)


@app.route('/')
def index():
    # redis_store.set("name", "summer")
    # 设置一个session 如果在redis中看到了session 说明配置成功
    session["name"] = "itcast"
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run(debug=True)
