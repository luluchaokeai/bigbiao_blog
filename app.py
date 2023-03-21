from flask import jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from apps.conf import ERROR_CODE
from apps.model.blogs_info import *
from apps.model.user_info import *
from apps.model.comments_info import *
from apps import create_app, jsonify_with_args
from exts import db

app = create_app()

manager = Manager(app=app)

migrate = Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)


@app.after_request
def return_error(response):
    """
    @param response: http返回值
    @return:通过返回值自定义错误信息
    """
    if response.status_code in ERROR_CODE:
        response_obj = {
            'success': False,
            'code': response.status_code,
            'data': {
                "error": ERROR_CODE.get(response.status_code)[1],
            },
        }
        try:
            if response.msg:
                response_obj['msg'] = response.msg
        except AttributeError:
            response_obj['msg'] = ERROR_CODE.get(response.status_code)[0]
        return jsonify_with_args(response_obj,code=response.status_code)
    return response


@manager.command
def create():
    # 删除全部表
    db.drop_all()
    # 重新建立
    db.create_all()


if __name__ == '__main__':
    print(app.url_map)
    manager.run()
