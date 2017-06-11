class Config(object):
    SECRET_KEY = 'qefrbeetb491'
    MONGODB_SETTINGS = {
        'db': 'iRichDB',
        'host': '127.0.0.1',
        'port': 27017
    }

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False