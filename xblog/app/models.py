#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from . import db


# class Post(db.Document):
#     author = db.StringField(max_length=50)
#     title = db.StringField(max_length=120, required=True)
#     tags = db.ListField(db.StringField(max_length=30))
#     time = db.DateTimeField(default=datetime.datetime.now())
#     content = db.StringField()


class Role(db.Model):
    """
    Roles Models
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role % r>' % self.name


class User(UserMixin, db.Model):
    """
    Users Models
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User % r>' % self.username

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])

        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def generate_reset_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset': self.id})

    def reset_password(self, token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('reset') != self.id:
            return False
        self.password = new_password
        db.session.add(self)
        return True


from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
