from flask import Blueprint
from controllers.UserController import get_users, add_user,get_user

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/api/users', methods=['GET'])(get_users)
user_bp.route('/api/user/<uuid:user_id>', methods=['GET'])(get_user)
user_bp.route('/api/users', methods=['POST'])(add_user)
