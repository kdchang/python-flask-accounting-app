from flask import render_template, Blueprint, redirect, url_for, request, flash, session, redirect, abort, flash
from webapp.models import User, Account
from webapp.forms import UserForm
from flask_login import UserMixin, LoginManager, login_required, current_user, login_user, logout_user, current_user
from webapp.extensions import login_manager
from passlib.hash import pbkdf2_sha256


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='../templates/main'
)

users = {'foo@bar.tld': {'pw': 'secret'}}

@login_manager.user_loader
def load_user(user_id):
    print('user_id', user_id)
    user = User.objects(id=user_id).first()
    return user

@main_blueprint.route('/')
def get_index():
    accounts = Account.objects
    form = UserForm()
    return render_template('main/index.html', accounts=accounts, form=form)

@main_blueprint.route('/login', methods=['GET'])
def get_login():
    form = UserForm()
    return render_template('main/login.html', form=form)

@main_blueprint.route('/login', methods=['POST'])
def post_login():
    form = UserForm()
    email = request.form.get('email')
    password = request.form.get('password')
    if form.validate_on_submit():
        user = User.objects(email=email).first()
        check_password = pbkdf2_sha256.verify(password, pbkdf2_sha256.hash(request.form.get('password')))

        if user != None and check_password:
            flash('Logged in successfully.')
            next = request.args.get('next')

            login_user(user)
            return redirect(next or url_for('main.get_index'))

    return render_template('main/login.html', form=form)

@main_blueprint.route('/signup', methods=['GET'])
def get_signup():
    form = UserForm()
    return render_template('main/signup.html', form=form)

@main_blueprint.route('/signup', methods=['POST'])
def post_signup():
    form = UserForm()
    if form.validate_on_submit():
        flash('Signedup in successfully.')
        email = request.form.get('email')
        username = request.form.get('username')
        password = pbkdf2_sha256.hash(request.form.get('password'))

        print('password', password)
        user = User(email=email, username=username, password=password)

        result = user.save()

        next = request.args.get('next')

        print('signup', result)
        # if not is_safe_url(next):
        #     return abort(400)
        return redirect(next or url_for('main.get_index'))

    return render_template('main/signup.html', form=form)

@main_blueprint.route('/logout', methods=['POST'])
@login_required
def post_logout():
    next = request.args.get('next')
    logout_user()
    # if not is_safe_url(next):
    #     return abort(400)
    return redirect(next or url_for('main.get_index'))
