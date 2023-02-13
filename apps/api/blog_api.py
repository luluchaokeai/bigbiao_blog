# -*- coding:UTF-8 -*-
from math import ceil

from apps.api import BaseResource
from apps.model.blogs_info import Blogs
from apps.utils import create_res_blog


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
            total_data = {'data_list': [], 'total_num': len(pagination.items), 'total_page':  ceil(len(pagination.items) / 10)}
            for blog in pagination.items:
                total_data['data_list'].append(create_res_blog(blog))
            self.response_obj['data'] = total_data
            self.response_obj['msg'] = "ok"
            return self.response_obj
