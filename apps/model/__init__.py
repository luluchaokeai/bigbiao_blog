# -*- coding:UTF-8 -*-
import datetime

from exts import db


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm


# 基本数据库模型类(没有创建时间)
class BaseModelNoCreateTime(db.Model):
    # 表示这是一个抽象类,只作为被继承的，不作为模型出现
    __abstract__ = True
    # id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="id")

    def save_update(self):
        """
        更新用户信息
        @return:True(更新成功)False(更新失败)
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            # 更新失败回滚
            db.session.rollback()
            print(e)
            return False
        return True


# 基本数据库模型类(带创建时间)
class BaseModelCreateTime(db.BaseModelNoCreateTime):
    # 表示这是一个抽象类,只作为被继承的，不作为模型出现
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="创建时间")


