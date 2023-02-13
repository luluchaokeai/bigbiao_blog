# -*- coding:UTF-8 -*-

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
