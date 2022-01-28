from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
   id = db.Column(db.Integer, primary_key = True,autoincrement=True)
   name = db.Column(db.String(100))
   passage_id = db.Column(db.String(24), index=True) 