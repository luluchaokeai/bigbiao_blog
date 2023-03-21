# -*- coding:UTF-8 -*-
from flask import Blueprint, Flask
from flask_caching import Cache
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:46
# software: PyCharm

db = SQLAlchemy()
cors = CORS()
cache = Cache()
auth = HTTPTokenAuth('Bearer')
api_bp = Blueprint('api', __name__)

api = Api(api_bp)
