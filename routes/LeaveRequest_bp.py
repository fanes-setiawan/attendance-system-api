from flask import Blueprint
from controllers.LeaveRequestController import get_leave_requests, add_leave_request, delete_leave_request

leave_request_bp = Blueprint('leave_request_bp', __name__)

leave_request_bp.route('/api/leave_requests', methods=['GET'])(get_leave_requests)
leave_request_bp.route('/api/leave_requests', methods=['POST'])(add_leave_request)
leave_request_bp.route('/api/leave_requests/<uuid:leave_id>', methods=['DELETE'])(delete_leave_request)
