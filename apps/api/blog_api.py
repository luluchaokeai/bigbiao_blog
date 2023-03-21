# -*- coding:UTF-8 -*-
from math import ceil

from flask import request

from apps.api import BaseResource
from apps.model.blogs_info import Blogs
from apps.utils import create_res_blog, get_blog_info
from exts import auth


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/13 16:17
# software: PyCharm

class BlogApi(BaseResource):
    def get(self, blog_id=None, page_num=1):
        # 获取单个文章
        if blog_id:
            blog = Blogs.query.get(blog_id)
            if blog:
                self.response_obj['data'] = create_res_blog(blog)
                self.response_obj['msg'] = "ok"
                return self.response_obj
            else:
                return self.return_error_msg("文章id不存在或输入有误")
        # 获取所有文章(主页啊,分类那种,需要采取分页)
        else:
            pagination = Blogs.query.order_by(Blogs.create_time).paginate(page_num, per_page=10, error_out=False)
            total_data = {
                'data_list': [], 'total_num': len(pagination.items),
                'total_page': ceil(len(pagination.items) / 10),
                "page": page_num}
            for blog in pagination.items:
                total_data['data_list'].append(create_res_blog(blog))
            self.response_obj['data'] = total_data
            self.response_obj['msg'] = "ok"
            return self.response_obj

    @auth.login_required
    def put(self):
        # 获取传递过来的数据
        blog = get_blog_info(request.form)
        blog.save_update()
        self.response_obj['data'] = "更新成功"
        self.response_obj['msg'] = "ok"
        return self.response_obj

    @auth.login_required
    def post(self):
        # 获取传递过来的数据
        blog = get_blog_info(request.form)
        blog.save_update()
        self.response_obj['data'] = "上传成功"
        self.response_obj['msg'] = "ok"
        return self.response_obj

 
