from flask import jsonify, request
from models.AttendanceHistoryModel import AttendanceHistory
from config import db

def get_attendance_history():
    history_records = AttendanceHistory.query.all()
    result = [record.to_dict() for record in history_records]
    return jsonify({"status": "success", "data": result}), 200

def add_attendance_history():
    data = request.get_json()
    new_history = AttendanceHistory(
        attendance_id=data['attendance_id'],
        change_reason=data['change_reason'],
        modified_by=data['modified_by'],
        modified_at=data.get('modified_at')
    )
    db.session.add(new_history)
    db.session.commit()
    return jsonify({"message": "Attendance history added successfully"}), 201
