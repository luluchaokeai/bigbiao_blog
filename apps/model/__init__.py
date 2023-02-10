# -*- coding:UTF-8 -*-
import datetime

from exts import db


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm

# 基本数据库模型类(带创建时间)
class BaseModelCreateTime(db.Model):
    # 表示这是一个抽象类,只作为被继承的，不作为模型出现
    __abstract__ = True
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="id")
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")


# 基本数据库模型类(没有创建时间)
class BaseModelNoCreateTime(db.Model):
    # 表示这是一个抽象类,只作为被继承的，不作为模型出现
    __abstract__ = True
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="id")



