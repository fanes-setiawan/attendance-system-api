from flask import Blueprint
from controllers.AttendanceHistoryController import get_attendance_history, add_attendance_history

attendance_history_bp = Blueprint('attendance_history_bp', __name__)

attendance_history_bp.route('/api/attendance_history', methods=['GET'])(get_attendance_history)
attendance_history_bp.route('/api/attendance_history', methods=['POST'])(add_attendance_history)
