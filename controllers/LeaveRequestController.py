from flask import jsonify, request
from models.LeaveRequestModel import LeaveRequest
from config import db

def get_leave_requests():
    leave_requests = LeaveRequest.query.all()
    result = [leave.to_dict() for leave in leave_requests]
    return jsonify({"status": "success", "data": result}), 200

def get_leave_request(leave_id):
    leave_request = LeaveRequest.query.get(str(leave_id))
    if leave_request:
        result = leave_request.to_dict()
        return jsonify({"status": "success", "data": result}), 200
    else:
        return jsonify({"status": "error", "message": "Leave request not found"}), 404

def add_leave_request():
    data = request.get_json()
    new_leave_request = LeaveRequest(
        user_id=data['user_id'],
        start_date=data['start_date'],
        end_date=data['end_date'],
        leave_type=data['leave_type'],
        reason=data.get('reason'),
        status=data.get('status', 'Pending')
    )
    db.session.add(new_leave_request)
    db.session.commit()
    return jsonify({"message": "Leave request added successfully"}), 201

def delete_leave_request(leave_id):
    leave_request = LeaveRequest.query.get(str(leave_id))
    if not leave_request:
        return jsonify({"error": "Leave request not found"}), 404

    db.session.delete(leave_request)
    db.session.commit()
    return jsonify({"message": "Leave request deleted successfully"}), 200
