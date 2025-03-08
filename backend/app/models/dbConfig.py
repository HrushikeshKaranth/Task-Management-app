from app import app
from flask_mysqldb import MySQL


# configuring mysql connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'task2'

mysql = MySQL(app)
# -----

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@localhost:3306/task2'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
