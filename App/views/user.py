from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required


from App.controllers import (
    create_user, 
    get_all_users,
    get_all_users_json,
    get_user
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#Create a new user
@user_views.route('/users', methods=['POST'])
def create_user():
    username = request.json.get("username")
    email = request.json.get("email")
    password = request.json.get("password")

    newuser = create_user(username, email, password)
    return (jsonify({"message":"created"}), 201) if newuser else (jsonify({"message":"could not create"}), 500)   

#Get all users
@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users_json()
    return jsonify(users)

#Get a specific user
@user_views.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user(user_id)
    return jsonify(user.toDict()) if user else (jsonify({"message": "entity with id not found"}), 404)
   

'''
# routes sir gave 
@user_views.route('/api/users')
def client_app():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/lol')
def lol():
    return 'lol'

@user_views.route('/static/users')
def static_user_page():
  return send_from_directory('static', 'static-user.html')
'''  