from flask import Blueprint
from controllers.AttendanceController import get_attendances, add_attendance , get_attendance

attendance_bp = Blueprint('attendance_bp', __name__)

#get all attendance
attendance_bp.route('/api/attendances', methods=['GET'])(get_attendances)

#get attendance by id
attendance_bp.route('/api/attendance/<uuid:attendance_id>', methods=['GET'])(get_attendance)

#add attendance
attendance_bp.route('/api/attendance', methods=['POST'])(add_attendance)

