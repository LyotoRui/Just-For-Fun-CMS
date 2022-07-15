from datetime import datetime
from flask_login import UserMixin
from app import db

class Customer(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Numeric, unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    