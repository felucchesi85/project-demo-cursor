from flask import Blueprint, request, jsonify
from app.controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)
user_controller = UserController()

@user_blueprint.route('/users/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user = user_controller.register_user(data['name'], data['email'])
    return jsonify({'name': user.name, 'email': user.email}), 201