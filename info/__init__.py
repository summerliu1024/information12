# 创建一个存放业务逻辑的包
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config

# 集成Sqlalchemy到flask


db = SQLAlchemy()


def set_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 10, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


redis_store = None  # type:StrictRedis


def create_app(config_name):
    set_log(config_name)
    app = Flask(__name__)
    # 集成配置类
    app.config.from_object(config[config_name])
    # 使用的时候才初始化
    db.init_app(app)
    # 连接redis
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT,decode_responses=True)

    # CSRFPROTECT保护
    # CSRFProtect(app)

    # 集成flask-session
    # 说明 flask中的session是保存用户数据的容器（上下文），而flask-session是指定session保存的路径
    Session(app)
    # 只使用一次，什么时候使用什么时候导入
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)

    return app
