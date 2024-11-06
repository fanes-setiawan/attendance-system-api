from flask import jsonify, request
from models.UserModel import User
from config import db


def get_users():
    users = User.query.all()
    result = [user.to_dict() for user in users]
    response = {
        "status": "success",
        "data": result,
        "message": "Users retrived successfully!",
    }
    return (jsonify(response), 200)


def get_user(user_id):
    user = User.query.get(str(user_id))
    if not user:
        return jsonify({"error": "User not found"}), 404

    result = user.to_dict()
    response = {
        "status": "success",
        "data": {"user": result},
        "message": "User retrieved successfuly!",
    }
    return (jsonify(response), 200)


def add_user():
    data = request.get_json()
    new_user = User(
        name=data["name"],
        email=data["email"],
        phone_number=data.get("phone_number"),
        password_hash=data["password_hash"],
    )
    db.session.add(new_user)
    db.session.commit()

    response = {
        "message": "User added successfully",
        "user": new_user.to_dict(),
    }
    return (jsonify(response), 201)


def update_user(user_id):
    user = User.query.get(str(user_id))
    if not user:
        return jsonify({"error": "user not found"}), 404

    update_data = request.get_json()

    user.name = update_data.get("name", user.name)
    user.email = update_data.get("email", user.email)
    user.phone_number = update_data.get("phone_number", user.phone_number)
    user.password_hash = update_data.get("password_hash", user.password_hash)

    db.session.commit()

    return jsonify({"message": "user updated successfully!", "user": user.to_dict()})


def patch_user(user_id):
    user = User.query.get(str(user_id))
    if not user:
        return jsonify({"error": "user not fount"}), 404

    patch_data = request.get_json()
    if "name" in patch_data:
        user.name = patch_data["name"]
    if "email" in patch_data:
        user.email = patch_data["email"]
    if "phone_number" in patch_data:
        user.phone_number = patch_data["phone_number"]
    if "password_hash" in patch_data:
        user.password_hash = patch_data["password_hash"]

    db.session.commit()
    return jsonify(
        {"message": "user partially updated successfully!", "user": user.to_dict()}
    )

def delete_user(user_id):
    user = User.query.get(str(user_id))
    if not user:
        return jsonify({'error' : 'user not fount'}),404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message':'user deleted successfully!'})