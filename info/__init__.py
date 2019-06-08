# 创建一个存放业务逻辑的包
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config

app = Flask(__name__)

# 集成配置类
app.config.from_object(config["develop"])
# 集成Sqlalchemy到flask
db = SQLAlchemy(app)
# 连接redis
redis_store = StrictRedis(host=config["develop"].REDIS_HOST, port=config["develop"].REDIS_PORT)

# CSRFPROTECT保护
CSRFProtect(app)

# 集成flask-session
# 说明 flask中的session是保存用户数据的容器（上下文），而flask-session是指定session保存的路径
Session(app)
