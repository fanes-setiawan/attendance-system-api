from config import db
import uuid
from sqlalchemy.dialects.mysql import CHAR

class Attendance(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=str(uuid.uuid4()))
    user_id = db.Column(CHAR(36), db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    check_in_time = db.Column(db.Time)
    check_out_time = db.Column(db.Time)
    status = db.Column(db.Enum('Hadir', 'Izin', 'Sakit', name='attendance_status'), default='Hadir')

    def to_dict(self):
        return {
            "id": str(self.id),
            "user_id": str(self.user_id),
            "date": self.date.isoformat(),
            "check_in_time": str(self.check_in_time),
            "check_out_time": str(self.check_out_time)if self.check_out_time else None,
            "status": self.status
        }
