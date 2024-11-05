from config import db
import uuid
from sqlalchemy.dialects.mysql import CHAR

class User(db.Model):
    id = db.Column(CHAR(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone_number = db.Column(db.String(15))
    password_hash = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "email": self.email,
            "phone_number": self.phone_number
        }
