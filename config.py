from redis import StrictRedis
class Config(object):
    SECRET_KEY = 'djfdshlfkhsdakfhasdklfhkpas;d'
    # 调试模式
    DEBUG = True
    # 数据库连接
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/information12'
    # 数据库跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis ip和端口配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    # flask-session的配置信息
    SESSION_TYPE = 'redis'
    # 指定存储session的存储对象
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置session签名
    SESSION_USE_SIGNER = True
    # 设置session永久保存与否
    SESSION_PERMANENT = False
    # 设置session的保存时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
