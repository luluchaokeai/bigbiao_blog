# -*- coding:UTF-8 -*-
import random
import string

from flask import request
from werkzeug.utils import secure_filename

from apps.api import BaseResource
from apps.conf.settings import SystemConfig
from apps.utils import allowed_file
from exts import auth


# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/13 14:43
# software: PyCharm

class FileApi(BaseResource):
    @auth.login_required
    def post(self):
        data = dict()
        file = request.files["file"]
        if file and allowed_file(file.filename):
            # 生成随机名字
            random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)) + secure_filename(
                file.filename)
            file_dir = SystemConfig.UPLOAD_DIR + "/" + random_name
            # 保存
            file.save(file_dir)
            # 定义返回值
            data["filename"] = random_name
            self.response_obj['data'] = data
            return self.response_obj
        else:
            return self.return_error_msg("请上传图片文件")
