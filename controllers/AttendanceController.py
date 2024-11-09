from flask import jsonify, request
from models.AttendanceModel import Attendance
from config import db

def get_attendances():
    attendance_records = Attendance.query.all()
    result = [record.to_dict() for record in attendance_records]
    return jsonify({"status": "success", "data": result}), 200

def get_attendance(attendance_id):
    attendance = Attendance.query.get(str(attendance_id))
    if attendance:
        result = attendance.to_dict()
        return jsonify({"status": "success", "data": result}), 200
    else:
        return jsonify({"status": "error", "message": "Attendance record not found"}), 404

def add_attendance():
    data = request.get_json()
    new_attendance = Attendance(
        user_id=data['user_id'],
        date=data['date'],
        check_in_time=data.get('check_in_time'),
        check_out_time=data.get('check_out_time'),
        status=data.get('status', 'Hadir')
    )
    db.session.add(new_attendance)
    db.session.commit()
    return jsonify({"message": "Attendance added successfully"}), 201
