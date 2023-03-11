from app import app, db
from flask import request, jsonify
from app.models.dbConfig import mysql
from app.models.users import Users, UserSchema
# Users controller
def users():
    if request.method == 'GET':
        if request.args.get('username'):
            username = request.args.get('username')
            cursor = mysql.connection.cursor()
            cursor.execute(
                ''' SELECT password,usertype,username FROM users where username like (%s) ''', [username])
            res = cursor.fetchall()
            cursor.close()
        else:
            email = request.args.get('email')
            cursor = mysql.connection.cursor()
            cursor.execute(
                ''' SELECT password,usertype,email FROM users where email like (%s) ''', [email])
            res = cursor.fetchall()
            cursor.close()
        return jsonify(res)
        # users = Users.query.all()
        # userdata = UserSchema(many = True)
        # return jsonify({'users' : userdata.dump(users)})

    if request.method == 'POST':
        res = request.get_json()
        username = res["username"]
        email = res["email"]
        firstname = res["firstname"]
        lastname = res["lastname"]
        password = res["password"]
        usertype = res["usertype"]
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' INSERT INTO users (username,email,firstname,lastname,password,usertype) VALUES(%s,%s,%s,%s,%s,%s)''', 
            [username, email, firstname, lastname, password, usertype])
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
        # res = request.get_json()
        # user = Users(
        # username = res["username"],
        # email = res["email"],
        # firstname = res["firstname"],
        # lastname = res["lastname"],
        # password = res["password"],
        # user_type = res["usertype"] or 'User',
        # designation = res["designation"] or 'none',
        # role = res["role"] or 'none',
        # status = 'Active')
        # db.session.add(user)
        # db.session.commit()
        # return f"User Data Added!"

    if request.method == 'DELETE':
        userId = request.args.get('id')
        user = Users.query.filter_by(id = userId).first()
        db.session.delete(user)
        db.session.commit()
        return f"User Deleted!"

#to reset password
def reset():
    email = request.args.get('email')
    cursor = mysql.connection.cursor()
    cursor.execute(
            ''' SELECT email, username, id FROM users where email like (%s) ''', [email])
    res = cursor.fetchall()
    cursor.close()
    return jsonify(res)

# update password
def updatepass():
    if request.method == 'PUT':
        res = request.get_json()
        id = res["id"]
        password = res["password"]
        cursor = mysql.connection.cursor()
        cursor.execute(
                ''' UPDATE users set password = (%s) WHERE id = (%s) ''', [password, id])
        mysql.connection.commit()
        res = cursor.fetchall()
        cursor.close()
        return f"done!"

#for login
def login():
    if request.args.get('username'):
        username = request.args.get('username')
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' SELECT password,usertype,email,username,id FROM users where username like (%s) ''', [username])
        res = cursor.fetchall()
        cursor.close()
    else:
        email = request.args.get('email')
        cursor = mysql.connection.cursor()
        cursor.execute(
            ''' SELECT password,usertype,email,username,id FROM users where email like (%s) ''', [email])
        res = cursor.fetchall()
        cursor.close()
    return jsonify(res)