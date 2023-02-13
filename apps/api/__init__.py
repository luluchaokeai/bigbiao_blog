# -*- coding:UTF-8 -*-
from flask_restful import Resource

from apps.utils import jsonify_with_args


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm
# redis配置

# BaseResource基类
class BaseResource(Resource):
    # 初始化返回数据
    def __init__(self):
        self.response_obj = {'success': True, 'code': 1, 'data': None, 'msg': 'ok'}

    def return_error_msg(self,msg):
        self.response_obj['code'] = 0
        self.response_obj['success'] = False
        self.response_obj['msg'] = msg
        return jsonify_with_args(self.response_obj, 400)