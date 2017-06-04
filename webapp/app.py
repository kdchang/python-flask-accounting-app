from flask import Flask, render_template, request, flash
import json
from .forms import ContactForm, MyForm
from .ext import db, app
from .models import User, TodoList

@app.route('/')
def index():
    return 'index'

@app.route('/accounts/create', methods=['GET'])
def get_create_account():
    form = ContactForm()
    return render_template('create_account.html', form=form)

@app.route('/accounts/create', methods=['POST'])
def post_create_account():
    pass

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    session = db.session
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            u1 = User(username='john', email='john@example.com')
            session.add(u1)
            session.commit()
            return 'sucess!!!'
    elif request.method == 'GET':
        for user in User.query.all():
            print(user.id, user.username, user.email)
        u = User.query.filter_by(username='john').first()
        u.email = 'john@example.vip.com'
        session.add(u)
        session.commit()
        session.close()

        print(User.query.filter_by(username='john').first().username)        
        u = User.query.filter_by(username='john').first()
        session.delete(u)
        session.commit()
        session.close()

        return render_template('contact.html', form=form)    

@app.route('/myform', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return 'hhhhhhh!'
    return render_template('myform.html', form=form)

if __name__ == '__main__':
    app.run(port=9999)