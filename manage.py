"""一，集成配置类
    二，sqlalchemy
    三，集成redis
    四，集成csrfprotect
    五，集成flask-session
    六，集成flask-script
    七，集成flask-migrate
    """

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db

# 工厂模式创建app
app = create_app("develop")

# 集成flask-script
manager = Manager(app)

# 集成flask-migrate 对数据库进行迁移
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    manager.run()
