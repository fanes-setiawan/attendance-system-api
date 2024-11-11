from config import app, db
from routes.Attendance_bp import attendance_bp
from routes.User_bp import user_bp
from routes.LeaveRequest_bp import leave_request_bp
from routes.AttendanceHistory_bp import attendance_history_bp

app.register_blueprint(attendance_bp)
app.register_blueprint(user_bp)
app.register_blueprint(leave_request_bp)
app.register_blueprint(attendance_history_bp)

db.create_all()
if __name__ == '__main__':
    app.run(debug=True)
