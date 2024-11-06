from flask import Blueprint
from controllers.UserController import get_users, add_user,get_user,update_user,patch_user,delete_user

user_bp = Blueprint('user_bp', __name__)

#get all user
user_bp.route('/api/users', methods=['GET'])(get_users)

#get by id
user_bp.route('/api/user/<uuid:user_id>', methods=['GET'])(get_user)

#add new user
user_bp.route('/api/users', methods=['POST'])(add_user)

#update user
user_bp.route('/api/user/<uuid:user_id>', methods=['PUT'])(update_user)

#patch user
user_bp.route('/api/user/<uuid:user_id>', methods=['PATCH'])(patch_user)

#delete user
user_bp.route('/api/user/<uuid:user_id>', methods=['DELETE'])(delete_user)

