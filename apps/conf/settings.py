import os.path


class SystemConfig:
    # 配置文件
    DEBUG = True
    # 数据库位置
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join("../bigbiao_blog.db")
    # 相对来说用来减少资源消耗
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 记录日志
    SQLALCHEMY_ECHO = True
    # 类似于加密密钥那种
    SECRET_KEY = 'x\x0f\xc9\xbd\xbf\xf0G\xf9\xae\x80\nX\x98\x83\xdfZ\xc0U\xde\xf1\xbb\xd4\xcf\x0e'
    # 当前项目路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # 静态资源路径
    STATIC_DIR = os.path.join(BASE_DIR, '../../static')
    # 上传文件路径
    UPLOAD_DIR = os.path.join(STATIC_DIR, 'uploads')
    # 允许上传的文件类型
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


class DevelopmentConfig(SystemConfig):
    ENV = "development"


class ProductionConfig(SystemConfig):
    ENV = "production"
    DEBUG = False
