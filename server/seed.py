from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db
from app import app
from models import db, User, Chore, ChoreList

with app.app_context():
    print("starting seed...")
    User.query.delete()
    Chore.query.delete()
    ChoreList.query.delete()
# Models go here!