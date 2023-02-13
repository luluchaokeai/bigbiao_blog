# -*- coding:UTF-8 -*-
from flask import request, jsonify

from apps.api import BaseResource
from apps.model.user_info import User
from apps.utils import jsonify_with_args, is_email
from exts import auth, cache


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm


class LoginApi(BaseResource):

    # 登录
    def post(self):
        data = dict()
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        print(request.form)
        if username and password:
            user = object()
            if is_email(username):
                user = User.query.filter(User.email == username).first()
            else:
                user = User.query.filter(User.nickname == username).first()
            try:
                print("---------------->")
                print(user)
                if user.verify_password(password):
                    token = user.generate_auth_token()
                    data['token'] = token
                    self.response_obj['data'] = data
                    self.response_obj['msg'] = "ok"
                    return jsonify_with_args(self.response_obj)
            except AttributeError:
                return self.return_error_msg("用户名或密码错误")
        return jsonify(error="请输入用户名密码"), 400


class UserApi(BaseResource):

    def get(self):
        # 返回用户信息(这里做的有点问题,但是本身就是单用户所以不考虑其它问题直接获取用户id为1的就行)
        user = User.query.get(1)
        data = dict()
        data['nickname'] = user.nickname
        data['email'] = user.email
        data['slogan'] = user.slogan
        data['head_url'] = user.head_url
        self.response_obj['data'] = data
        self.response_obj['msg'] = "ok"
        return self.response_obj

    @auth.login_required
    def put(self):
        # 获取传递过来的数据
        args = request.form
        nickname = args.get('nickname', "")
        email = args.get('email', "")
        head_url = args.get('head_url', "")
        slogan = args.get('slogan', "")
        user = User.verify_auth_token(cache.get('token'))
        user.nickname = nickname
        user.email = email
        user.slogan = slogan
        user.head_url = head_url
        # 更新信息
        user.save_update()
        self.response_obj['data'] = "更新成功"
        self.response_obj['msg'] = "ok"
        return self.response_obj
