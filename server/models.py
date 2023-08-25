from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates

from config import db

# Models go here!

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique = True, nullable = False)
    _password_hash = db.Column(db.String, nullable = False)


class Chore(db.Model):
    __tablename__ = 'chores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    value = db.Column(db.Integer)
    completed = db.Column(db.Boolean)



class ChoreList(db.Model):
    __tablename__ = 'chorelists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeigKey('users.id'))
    chore_id = db.Column(db.Integer, db.ForeignKey('chores.id'))
    value = db.Column(db.Integer)