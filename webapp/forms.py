from flask_mongoengine.wtf import model_form
from .models import User, Account

UserForm = model_form(User)
AccountForm = model_form(Account)

# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField
# from wtforms.validators import DataRequired

# class AccountForm(FlaskForm):
#     name = StringField('name', validators=[DataRequired()])
#     type = StringField('type', validators=[DataRequired()])
#     cost = IntegerField('cost', validators=[DataRequired()])