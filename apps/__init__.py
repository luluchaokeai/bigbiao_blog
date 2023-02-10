# -*- coding:UTF-8 -*-
from flask import Flask

from apps.api import REDIS_CONFIG
from apps.api.blog_api import blog_bp
from exts import *
from apps.conf.settings import DevelopmentConfig


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm
def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(DevelopmentConfig)

    db.init_app(app=app)
    # 跨域相关
    cors.init_app(app=app, supports_credentials=True)
    cache.init_app(app=app, config=REDIS_CONFIG)
    # 注册蓝图
    app.register_blueprint(blog_bp)
    return app
