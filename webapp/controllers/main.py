from flask import (render_template,
                   current_app,
                   Blueprint,
                   redirect,
                   url_for,
                   request,
                   flash,
                   session,
                   redirect,
                   request)
from functools import wraps

from ..forms import AccountForm
from ..models import Account

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

from functools import wraps
from flask import request, Response


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@main_blueprint.route('/')
def index():
    accounts = Account.objects
    return render_template('main/index.html', accounts=accounts)

@main_blueprint.route('/create/accounts')
@requires_auth
def get_create_account():
    form = AccountForm()
    return render_template('main/create_account.html', form=form)    

@main_blueprint.route('/create/accounts', methods=['POST'])
def post_create_account():
    form = AccountForm()
    print('form.validate_on_submit()', form.validate_on_submit())
    print('request.method', request.method)
    if request.method == 'POST' and form.validate_on_submit():
        # do something
        title = request.form.get('title')
        type = request.form.get('type')
        cost = request.form.get('cost')
        new_account = Account(title=title, type=type, cost=cost)
        new_account.save()
        print('new_account', new_account)
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('main.get_create_account'))
        