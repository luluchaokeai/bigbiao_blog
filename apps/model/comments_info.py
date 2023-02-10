# -*- coding:UTF-8 -*-
from apps.model import BaseModelCreateTime
from exts import db


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 14:28
# software: PyCharm

# 评论表
class Comments(BaseModelCreateTime):
    __tablename__ = 'comments'
    # 评论内容
    comment_content = db.Column(db.Text, nullable=False, comment="评论内容")
    # 评论文章id(可以是回复评论的，固可以为空)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), comment="评论文章id")
    # 父评论id(可以是回复博客的，固可以为空)
    parent_id = db.Column(db.Integer, comment="父评论id")
    # 评论用户id(注意这个表不是用户表，是单独的评论用户表)
    user_id = db.Column(db.Integer, db.ForeignKey('comment_user.id'), comment="评论人id")
