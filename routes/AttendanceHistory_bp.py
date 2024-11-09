from flask import Blueprint
from controllers.AttendanceHistoryController import get_attendance_historys, add_attendance_history, get_attendance_history

attendance_history_bp = Blueprint('attendance_history_bp', __name__)

#get all attendance history
attendance_history_bp.route('/api/attendance_historys', methods=['GET'])(get_attendance_historys)


attendance_history_bp.route('/api/attendance_history/<uuid:history_id>', methods=['GET'])(get_attendance_history)

#add attendance history
attendance_history_bp.route('/api/attendance_history', methods=['POST'])(add_attendance_history)
