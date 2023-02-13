# -*- coding:UTF-8 -*-
from flask import Flask

from apps.api.blog_api import BlogApi
from apps.api.file_api import FileApi
from apps.api.user_api import *
from apps.conf import REDIS_CONFIG
from exts import *
from apps.conf.settings import DevelopmentConfig


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm

def add_resource(api):
    # 登录
    api.add_resource(LoginApi, '/login')
    # 文件上传
    api.add_resource(FileApi, '/file/upload')
    # 用户相关
    api.add_resource(UserApi, '/user')
    api.add_resource(BlogApi, '/blog', '/blog/<int:blog_id>', '/blog/all/<int:page_num>')


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(DevelopmentConfig)

    db.init_app(app=app)
    # 跨域相关
    cors.init_app(app=app, supports_credentials=True)
    # 缓存相关
    cache.init_app(app=app, config=REDIS_CONFIG)
    add_resource(api)
    # 注册蓝图
    app.register_blueprint(api_bp)
    return app
