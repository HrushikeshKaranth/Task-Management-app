# from datetime import datetime
# from flask_marshmallow import Marshmallow
from app import db, ma
from sqlalchemy.sql import func

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    password = db.Column(db.String(100), nullable = False)
    firstname = db.Column(db.String(100), nullable = False)
    lastname = db.Column(db.String(100), nullable = False)
    usertype = db.Column(db.Enum('Admin','Sub_Admin','User'), nullable = False)
    timestamp = db.Column(db.DateTime, default=func.now())

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users