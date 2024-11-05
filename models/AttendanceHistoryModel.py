from config import db
import uuid
from sqlalchemy.dialects.mysql import CHAR
from datetime import datetime

class AttendanceHistory(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=str(uuid.uuid4()))
    attendance_id = db.Column(CHAR(36), db.ForeignKey('attendance.id'), nullable=False)
    change_reason = db.Column(db.Text, nullable=False)
    modified_by = db.Column(CHAR(36), db.ForeignKey('user.id'), nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": str(self.id),
            "attendance_id": str(self.attendance_id),
            "change_reason": self.change_reason,
            "modified_by": str(self.modified_by),
            "modified_at": self.modified_at
        }
