# -*- coding:UTF-8 -*-


from flask import Blueprint
from flask_restful import Api, Resource, fields, marshal

from apps.model.blogs_info import BlogType

# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:30
# software: PyCharm

blog_bp = Blueprint('/blog', __name__)
api = Api(blog_bp)

blog_type_fields = {
    'id': fields.Integer(),
    'name': fields.String(attribute="type_name"),
    'crate_time': fields.DateTime()
}
temple_fields = {
    'state': 200,
    'msg': 'success',
    'data': []
}


class BlogTypeApi(Resource):
    @staticmethod
    def get():
        types = BlogType.query.all()
        res = temple_fields
        res['data'] = marshal(types, blog_type_fields)
        return res


api.add_resource(BlogTypeApi, '/type')
