from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
CORS(app)

# SQLAlchemy and Migrate Config
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root123@localhost:3306/task2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
#-----

# Importing models after creating Migrate configs
from app.models.users import *
#-----

# Registering routes
from app.routes.routes import routes
app.register_blueprint(routes)
#-----
