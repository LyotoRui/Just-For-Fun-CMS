from sqlalchemy import JSON
from app import db

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    orders = db.Column(db.JSON)

    def __init__(self, id: int, first_name: str, last_name: str, email: str, phone: str, orders: JSON) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.orders = orders

    def __repr__(self) -> str:
        return f'Customer {self.id}'