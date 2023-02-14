# -*- coding:UTF-8 -*-
from sqlalchemy import MetaData

from apps.model import *
from exts import db


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:33
# software: PyCharm


# 分类表
class BlogType(BaseModelCreateTime):
    __tablename__ = 'blog_type'
    # 分类名
    type_name = db.Column(db.String(50), nullable=False, comment="分类名")


# 标签
class BlogTag(BaseModelCreateTime):
    __tablename__ = 'blog_tag'
    # 标签名
    tag_name = db.Column(db.String(50), nullable=False, comment="标签名")


# 博客和标签关系表(因为这个不同于正常的一对多的一个关系，建立联系好像实现不了，固采用关系表)
blog_tag_map = db.Table(
    'blog_map',
    db.Column('tag_id', db.Integer, db.ForeignKey('blog_tag.id'), comment="标签id"),
    db.Column('blog_id', db.Integer, db.ForeignKey('blog.id'), comment="文章id"),
    # 两个id互相约束，即每一个都只能出现一次
    db.PrimaryKeyConstraint('tag_id', 'blog_id')
)


# 博客表
class Blogs(BaseModelCreateTime):
    __tablename__ = 'blog'
    # 标题
    title = db.Column(db.String(100), nullable=False, comment="标题")
    # 正文
    content = db.Column(db.Text, nullable=False, comment="正文")
    # 观看数
    see_num = db.Column(db.Integer, default=0, comment="观看数")
    # 更新时间
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, comment="更新时间")
    # 是否删除
    is_del = db.Column(db.Boolean, default=1, comment='是否删除')
    # 分类id
    type_id = db.Column(db.Integer, db.ForeignKey('blog_type.id'), comment="分类id")
    # 创建人id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, comment="创建人id")
    # 通过中间表建立联系,lazy为joined在网上搜是遇到大量数据的时候比较快的解决方法(由于本身就是一个练手和自己建议博客的一个搭建，固没有研究，直接参考的结论)
    tags = db.relationship('BlogTag', secondary=blog_tag_map, backref=db.backref('blogs', lazy='joined'),
                           lazy="joined")

    def save_update(self):
        pass
