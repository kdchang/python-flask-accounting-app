import os
from flask import Flask

from .models import db
from .controllers.main import main_blueprint
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine

csrf = CSRFProtect()
db = MongoEngine()

def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    app = Flask(__name__)
    csrf.init_app(app)
    app.config.from_object(object_name)

    # db.init_app(app)
    db = MongoEngine(app)
    app.register_blueprint(main_blueprint)

    return app