from config import db
import uuid
from sqlalchemy.dialects.mysql import CHAR

class LeaveRequest(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(CHAR(36), db.ForeignKey('user.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    leave_type = db.Column(db.Enum('Tahunan', 'Sakit', 'Lainnya', name='leave_type'), default='Tahunan')
    reason = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('Pending', 'Disetujui', 'Ditolak', name='leave_status'), default='Pending')

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "start_date": self.start_date,
            "end_date": self.end_date,
            "leave_type": self.leave_type,
            "reason": self.reason,
            "status": self.status
        }
