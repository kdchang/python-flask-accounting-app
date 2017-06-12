import os
from flask import Flask
from .models import db
from .controllers.main import main_blueprint
from .controllers.account import account_blueprint
from .extensions import csrf, login_manager, db, toolbar, oauth


def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    app = Flask(__name__)
    app.config.from_object(object_name)

    csrf.init_app(app)
    login_manager.init_app(app)

    db.init_app(app)
    toolbar.init_app(app)
    oauth.init_app(app)

    app.secret_key = 'Secret Menu'
    app.register_blueprint(main_blueprint)
    app.register_blueprint(account_blueprint, url_prefix='/accounts')

    return app