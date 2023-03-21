# -*- coding:UTF-8 -*-
import re

# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 15:20
# software: PyCharm
# token有效时间
JWT_EXPIRY_SECOND = 30 * 60
# redis配置(多半不会使用)
REDIS_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_PASSWORD': 'bigbiao'
}

ERROR_CODE = {
    301: ["	Moved Permanently", "资源被永久转移"],
    400: ["Bad Request", "错误请求"],
    401: ["Unauthorized	", "未授权访问"],
    403: ["Forbidden", "拒绝执行"],
    404: ["Not Found", "没有找到"],
    405: ["Method Not Allowed", "方法不被允许"],
    500: ["Internal Server Error", "服务器错误"],
}

EMAIL_REG = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')