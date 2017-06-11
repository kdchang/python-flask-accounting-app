from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine
from flask_debugtoolbar import DebugToolbarExtension


login_manager = LoginManager()
csrf = CSRFProtect()
db = MongoEngine()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.get_login'
login_manager.login_message = 'Please LOG IN'
login_manager.login_message_category = 'info'
toolbar = DebugToolbarExtension()
