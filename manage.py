"""一，集成配置类
    二，sqlalchemy
    三，集成redis
    四，集成csrfprotect
    五，集成flask-session
    六，集成flask-script
    七，集成flask-migrate
    """

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config

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
# 集成flask-script
manager = Manager(app)

# 集成flask-migrate 对数据库进行迁移
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route('/')
def index():
    # redis_store.set("name", "summer")
    # 设置一个session 如果在redis中看到了session 说明配置成功
    session["name"] = "itcast"
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    manager.run()
