from flask import jsonify, request
from models.UserModel import User
from config import db

def get_users():
    users = User.query.all()
    result = [user.to_dict() for user in users]
    return jsonify({"status": "success", "data": result}), 200

def add_user():
    data = request.get_json()
    new_user = User(
        name=data['name'],
        email=data['email'],
        phone_number=data.get('phone_number'),
        password_hash=data['password_hash']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added successfully"}), 201
