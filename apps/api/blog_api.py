# -*- coding:UTF-8 -*-
import jwt
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource

from apps.conf import settings
from apps.model.user_info import User
from exts import auth
from apps.utils import verify_token

# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm

blog_bp = Blueprint('/blog', __name__)
api = Api(blog_bp)


class Login(Resource):
    @auth.login_required
    def get(self):
        return {'data': 'Protected data'}, 200

    def post(self):
        args = request.form
        username = args.get("username", "")
        password = args.get("password", "")
        if username and password:
            users = []
            users.extend(User.query.filter(User.nickname == username))
            users.extend(User.query.filter(User.email == username))
            for user in users:
                if user.verify_password(password):
                    token = user.generate_auth_token()
                    return {'token': token}, 200
            else:
                msg = "用户名或密码错误"
                return jsonify(error=msg), 400
        return jsonify(error="请输入用户名密码"), 400


api.add_resource(Login, '/login')
