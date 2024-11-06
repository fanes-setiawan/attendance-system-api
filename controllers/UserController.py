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
    return (
        jsonify(response),
        200,
    )


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
    return (
        jsonify({"message": "User added successfully", "user": new_user.to_dict()}),
        201,
    )
