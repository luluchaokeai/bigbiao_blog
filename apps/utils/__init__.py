# -*- coding:UTF-8 -*-
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
