# -*- coding:UTF-8 -*-
from werkzeug.security import generate_password_hash

from apps.model import BaseModelCreateTime
from exts import db


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 11:26
# software: PyCharm

# 用户模型类
class User(BaseModelCreateTime):
    __tablename__ = 'user'
    # 昵称
    nickname = db.Column(db.String(48), nullable=False, comment="昵称")
    # 邮箱
    email = db.Column(db.String(48), nullable=False, comment="邮箱")
    # 密码
    password = db.Column(db.String(128), comment="密码")
    # 头像
    head_url = db.Column(db.String(32), comment="头像")
    # 个性签名
    slogan = db.Column(db.String(64), default='生活十分有趣，而我万分沙雕.', comment='Slogan')
    # 详细介绍(关于我页面内容)
    detail = db.Column(db.Text, comment="详细介绍")
    # 添加反向引用(指出创建的文章)
    blogs = db.relationship('blog', backref='user')

    def hash_password(self, password):
        """
        密码加密
        :param password:原始密码
        :return:
        """
        self.password = generate_password_hash(password)
        return self.password




class CommentsUser(BaseModelCreateTime):
    __tablename__ = 'comment_user'
    # 昵称
    nickname = db.Column(db.String(50), nullable=False, comment="昵称")
    # 邮箱
    email = db.Column(db.String(20), nullable=False, comment="邮箱")

    # 重写__repr__(即直接打印这个类的时候)
    def __repr__(self):
        return '<访客User %r>' % self.nickname
