from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
from wtforms import validators, ValidationError

class MyForm(FlaskForm):
    '''
    MyForm
    '''
    name = TextField('name', validators=[validators.DataRequired()])

class ContactForm(FlaskForm):
    name = TextField("Name Of Student",[validators.DataRequired("Please enter your name.")])
    Gender = RadioField('Gender', choices = [('M','Male'), ('F','Female')])
    Address = TextAreaField("Address")
    email = TextField('Email', [validators.DataRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    Age = IntegerField('age')
    language = SelectField('Languages', choices=[('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField('Send')
