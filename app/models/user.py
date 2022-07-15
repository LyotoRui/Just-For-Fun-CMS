
from datetime import datetime
import enum
from flask_login import UserMixin
from app import db

class UserRole(enum.IntEnum):
    SUPER_USER = 0
    OWNER = 1
    ADMIN = 2
    MODERATOR = 3
    MANAGER = 4

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow())

    def __init__(self, login: str, password: str, email: str, first_name: str, last_name: str, role: int) -> None:
        self.login = login
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

