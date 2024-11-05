from flask import Blueprint
from controllers.AttendanceController import get_attendance, add_attendance

attendance_bp = Blueprint('attendance_bp', __name__)

attendance_bp.route('/api/attendance', methods=['GET'])(get_attendance)
attendance_bp.route('/api/attendance', methods=['POST'])(add_attendance)
