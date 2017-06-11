from mongoengine import *
from flask_login import UserMixin


db = connect('iRichDB')

class User(Document, UserMixin):
    username = StringField(max_length=20)
    email = StringField(max_length=36)
    password = StringField(max_length=100)
    #pass

class Account(Document):
    title = StringField(max_length=50)
    types = StringField(max_length=50)
    cost = IntField(max_length=50)

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Account(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(36))
#     type = db.Column(db.String(36))
#     cost = db.Column(db.String(36))

#     def init(self, title, type, cost):
#         title = self.title
#         type = self.type
#         cost = self.cost