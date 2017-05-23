import time
from .ext import db
from flask_login import UserMixin
import time

class TodoList(db.Model):
    __tablename__ = 'todolist'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(1024), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    create_time = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, title, status):
        self.user_id = user_id
        self.title = title
        self.status = status
        self.create_time = time.time()

class Account(db.Model):
    __tablename__  = 'account'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(24), nullable=False)
    type = db.Column(db.String(36), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.Integer, nullable=False)

    def __init__(self, title, type, cost, time, created_at):
        self.title = title
        self.type = type
        self.cost = cost
        self.time = time
        self.created_at = time.time()

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(24), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email
