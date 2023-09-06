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

    Chore1 = ["Dishes", "Empty out dishrack and do dirty dishes", 2, False]
    Chore2 = ["Vacuum", "Vacuum the living room", 3, False]
    Chore3 = ["Clean stove", "Wipe down and clean under the grate of the stove", 3, False]
    Chore4 = ["Clean toilet", "Scrub toilet bowl with bleach and wipe down outside of bowl", 4, False]
    Chore5 = ["Kitty litter", "Removed poo and pee from litter box", 3, False]
    Chore6 = ["Replace kitty litter", "Removed poo and pee from litter box", 4, False]
    Chore7 = ["Make bed", "Make the bed, tucking in sheets, and organizing pillows", 1, False ]
    Chore8 = ["Feed the boys", "Give the cats food", 1, False]
    Chore9 = ["Wash laundry", "Sort and wash laundry", 3, False]
    ChoreList1 = []

# Models go here!