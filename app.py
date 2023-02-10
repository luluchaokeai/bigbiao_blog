from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apps.model.blogs_info import *
from apps.model.user_info import *
from apps.model.comments_info import *
from apps import create_app
from exts import db

app = create_app()
manager = Manager(app=app)

migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@manager.command
def create():
    # 删除全部表
    db.drop_all()
    # 重新建立
    db.create_all()


if __name__ == '__main__':
    manager.run()
