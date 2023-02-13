# -*- coding:UTF-8 -*-
import datetime
import re

from flask import make_response, jsonify

from apps.model.user_info import User
from exts import auth
from apps.conf.settings import SystemConfig


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
    return make_response(jsonify(data), code, *args)


email_reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def is_email(email):
    """
    # 判断是不是邮箱
    @param email: 邮箱
    @return: True or False
    """
    if re.fullmatch(email_reg, email):
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
    # 生成blog的字典
    @param blog: blog对象
    @return: 根据该对象生成的字典元素
    """
    data = dict()
    data['title'] = blog.title
    data['content'] = blog.content
    data['see_num'] = blog.see_num
    data['create_time'] = datetime.datetime.timestamp(blog.create_time)
    data['update_time'] = datetime.datetime.timestamp(blog.update_time)
    return data
