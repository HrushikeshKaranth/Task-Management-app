from flask import Blueprint
from app.controllers.UserController import users, updatepass, reset, login

# Creating routes Blueprint
routes = Blueprint('routes', __name__)
#-----

#for login
routes.route('/login', methods = ['GET'])(login)

#for registering
routes.route("/register", methods=['POST'])(users)

#to reset password
routes.route("/resetpass")(reset)

# reset password
routes.route("/updatepass", methods=['PUT'])(updatepass)

# delete users
routes.route("/delete", methods=['DELETE'])(users)
