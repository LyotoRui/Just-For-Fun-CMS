from datetime import datetime
from flask_login import UserMixin
from app import db
from app.routes.cp_auth import login

class Customer(UserMixin, db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Numeric, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    def __init__(self, login: str, password: str, email: str, phone: str, first_name: str, last_name: str) -> None:
        self.login = login
        self.password = password
        self.email = email
        self.phone = phone
        self.first_name = first_name
        self.last_name = last_name

