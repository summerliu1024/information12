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
from info.models import *

# 工厂模式创建app
app = create_app("develop")

# 集成flask-script
manager = Manager(app)

# 集成flask-migrate 对数据库进行迁移
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@manager.option('-n', '--name', dest="name")
@manager.option('-p', '--password', dest="password")
def createsuperuser(name, password):

    if not all([name, password]):
        print("参数不足")

    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    print("添加成功")

if __name__ == '__main__':
    # 运行当前Flask应用程序
    manager.run()
