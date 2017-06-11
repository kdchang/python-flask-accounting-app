from flask import render_template, Blueprint, redirect, url_for, request, flash, session, redirect
from flask_login import login_required
from ..forms import AccountForm
from ..models import Account


account_blueprint = Blueprint(
    'account',
    __name__,
    template_folder='../templates/main'
)

@account_blueprint.route('/create')
def get_create_account():
    form = AccountForm()
    return render_template('accounts/create_account.html', form=form)    

@account_blueprint.route('/create', methods=['POST'])
def post_create_account():
    form = AccountForm()
    print('form.validate_on_submit()', form.validate_on_submit())
    print('request.method', request.method)
    if request.method == 'POST' and form.validate_on_submit():
        # do something
        title = request.form.get('title')
        types = request.form.get('types')
        cost = request.form.get('cost')
        new_account = Account(title=title, types=types, cost=cost)
        new_account.save()
        print('new_account', new_account)
        return redirect(url_for('main.get_index'))
    else:
        return redirect(url_for('main.get_create_account'))

@account_blueprint.route('/<account_id>/', methods=['GET'])
def get_account(account_id):
    form = AccountForm()
    account = Account.objects(id=account_id).first()
    return render_template('accounts/account.html', account=account, form=form)

@account_blueprint.route('/<account_id>/update', methods=['GET'])
@login_required
def get_update_account(account_id):
    account = Account.objects(id=account_id).first()
    form = AccountForm()
    return render_template('accounts/update_account.html', account=account, form=form)

@account_blueprint.route('/<account_id>/update', methods=['POST'])
@login_required
def post_update_account(account_id):
    form = AccountForm()
    if request.method == 'POST' and form.validate_on_submit():
        # do something
        title = request.form.get('title')
        types = request.form.get('types')
        cost = request.form.get('cost')
        account = Account.objects(id=account_id).first()
        #print('account', account.title)

        account.update(title=title)
        account.update(types=types)
        account.update(cost=cost)
        #account = Account.objects(id=account_id).update_one(set_title=title, set_type=type, set_cost=cost)
        return redirect(url_for('main.get_index'))
    else:
        return redirect(url_for('main.get_update_account'))

@account_blueprint.route('/<account_id>/delete', methods=['POST'])
@login_required
def post_delete_account(account_id):
    account = Account.objects(id=account_id).first()
    account.delete()
    return redirect(url_for('main.get_index'))
