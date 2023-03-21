# -*- coding:UTF-8 -*-
import datetime
import re

from flask import make_response, jsonify

from apps.conf import EMAIL_REG
from apps.conf.settings import SystemConfig
from apps.model.blogs_info import Blogs, BlogTag
from apps.model.user_info import User
from exts import auth


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/10 15:56
# software: PyCharm

@auth.verify_token
def verify_token(token):
    """
    @param token:token
    @return:token没过期返回true,过期返回false
    """
    # 检测cookie
    user = User.verify_auth_token(token=token)
    if user:
        return True
    else:
        return False


# 格式化返回包
def jsonify_with_args(data, code=200, *args):
    """
    返回json数据同时修改返回状态码,etc
    :param data: 返回的数据
    :param code: 状态码
    :param args: 其它参数
    :return: response对象
    """
    assert isinstance(data, dict)
    resp = make_response(jsonify(data), code, *args)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    print(resp)
    return resp

def is_email(email):
    """
    # 判断是不是邮箱
    @param email: 邮箱
    @return: True or False
    """
    if re.fullmatch(EMAIL_REG, email):
        return True
    return False


def allowed_file(filename):
    """
    # 判断是不是允许上传的文件
    @param filename:文件名
    @return: True or False
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in SystemConfig.ALLOWED_EXTENSIONS


def create_res_blog(blog):
    """
    # 生成blog的字典,返回
    @param blog: blog对象
    @return: 根据该对象生成的字典元素
    """
    data = dict()
    data['id'] = blog.id
    data['title'] = blog.title
    data['content'] = blog.content
    data['see_num'] = blog.see_num
    data['create_time'] = datetime.datetime.timestamp(blog.create_time)
    data['update_time'] = datetime.datetime.timestamp(blog.update_time)
    return data


def get_blog_info(args):
    """
    # 创建blog的字典,写入
    @param args: request.form中的args
    @return: 根据该对象生成的字典元素
    """
    title = args.get('title', "")
    content = args.get('content', "")
    create_time = args.get('update_time', "")
    update_time = args.get('create_time', "")
    user_id = args.get('user_id', "")
    tags = args.getlist('tags')
    blog = Blogs()
    blog.title = title
    blog.content = content
    blog.create_time = create_time
    blog.update_time = update_time
    blog.user_id = user_id
    tags = [tag for tag in BlogTag.query().filter(BlogTag.id.in_(tags))]
    # 更新信息
    blog.tags = tags
    return blog
