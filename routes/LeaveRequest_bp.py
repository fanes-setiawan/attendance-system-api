from flask import Blueprint
from controllers.LeaveRequestController import get_leave_requests, add_leave_request, delete_leave_request , get_leave_request

leave_request_bp = Blueprint('leave_request_bp', __name__)

#get all leave
leave_request_bp.route('/api/leave_requests', methods=['GET'])(get_leave_requests)


#get leave by id
leave_request_bp.route('/api/leave_request/<uuid:leave_id>', methods=['GET'])(get_leave_request)

#add leave
leave_request_bp.route('/api/leave_requests', methods=['POST'])(add_leave_request)

#delete leave
leave_request_bp.route('/api/leave_requests/<uuid:leave_id>', methods=['DELETE'])(delete_leave_request)
