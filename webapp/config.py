import os

class Config(object):
    SECRET_KEY = 'qefrbeetb491'
    MONGODB_SETTINGS = {
        'db': 'iRichDB',
        'host': '127.0.0.1',
        'port': 27017
    }

    FACEBOOK_APP_ID = os.environ['FACEBOOK_APP_ID']
    FACEBOOK_APP_SECRET = os.environ['FACEBOOK_APP_SECRET']

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_PANELS = ['flask_mongoengine.panels.MongoDebugPanel']
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///../database.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True    