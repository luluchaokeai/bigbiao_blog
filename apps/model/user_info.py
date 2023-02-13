# -*- coding:UTF-8 -*-
# import datetime
import time
import datetime

import jwt
from jwt import PyJWTError
from werkzeug.security import generate_password_hash, check_password_hash

from apps.conf import settings
from apps.model import BaseModelCreateTime
from exts import db, cache


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
    password = db.Column(db.String(128), comment="密码", nullable=False)
    # 头像
    head_url = db.Column(db.String(32), comment="头像")
    # 个性签名
    slogan = db.Column(db.String(64), default='生活十分有趣，而我万分沙雕.', comment='Slogan')
    # 详细介绍(关于我页面内容)
    detail = db.Column(db.Text, comment="详细介绍")
    # 添加反向引用(指出创建的文章)
    blogs = db.relationship('Blogs', backref='user')

    def hash_password(self, password):
        """
        密码加密
        :param password:原始密码
        :return:加密后密码
        """
        self.password = generate_password_hash(password)
        return self.password

    def verify_password(self, password):
        """
        检查密码
        @param password:用户输入的密码
        @return:Boolean
        """
        return check_password_hash(self.password, password)

    def generate_auth_token(self):
        """
        生成token，有效时间30min
        :return: token
        """
        # payload 生成密钥的参数
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),  # 过期时间
        }
        # key:密钥,
        # algorithm:算法，算法是SHA-256
        # SHA-256:密码散列函数算法.256字节长的哈希值（32个长度的数组）---》16进制字符串表示，长度为64。信息摘要，不可以逆
        token = jwt.encode(payload, settings.SystemConfig.SECRET_KEY, algorithm='HS256')
        # 由于只有一个用户固缓存里面直接为token(多用户的话要依据情况修改)
        cache.set("token", token, int(datetime.datetime.timestamp(payload['exp'])))
        return token

    @staticmethod
    def verify_auth_token(token):
        """
        @param token:token
        @return:没过期返回User对象,否则返回None
        """
        try:
            # 返回之前生成token的时候的字典，字典种包含id和exp
            data = jwt.decode(token, settings.SystemConfig.SECRET_KEY, algorithms=['HS256'])
            user = User.query.filter(User.id == data['user_id']).first()
            if user and data['exp'] > int(time.time()):  # 如果用户存在，并且没有过期
                return user
            else:
                return None
        except PyJWTError as e:
            return None

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


class CommentsUser(BaseModelCreateTime):
    __tablename__ = 'comment_user'
    # 昵称
    nickname = db.Column(db.String(50), nullable=False, comment="昵称")
    # 邮箱
    email = db.Column(db.String(20), nullable=False, comment="邮箱")

    # 重写__repr__(即直接打印这个类的时候)
    def __repr__(self):
        return '<访客User %r>' % self.nickname
