# -*- coding:UTF-8 -*-
from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# author:28795
# contact: 2879503947@qq.com
# datetime:2023/2/8 10:46
# software: PyCharm

db = SQLAlchemy()
cors = CORS()
cache = Cache()
