# from datetime import datetime
# from flask_marshmallow import Marshmallow
from app import db, ma
from sqlalchemy.sql import func

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(500), nullable = False)
    assignto = db.Column(db.String(100), nullable = False)
    startdate = db.Column(db.String(100), nullable = False)
    enddate = db.Column(db.String(100), nullable = False)
    deadline = db.Column(db.String(100), nullable = False)
    taskstatus = db.Column(db.Enum('Done', 'Todo', 'In Progress', 'Ready For Test'), nullable = False)
    screenshot = db.Column(db.String(500), nullable = False)

class TaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tasks