from sqlalchemy import JSON
from app import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime(tzinfo=None))
    is_fast = db.Column(db.Boolean, default=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    served_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    products = db.Column(db.JSON, nullable=False)

    def __init__(self, id: int, timestamp: datetime, is_fast: bool, customer_id: int, products: JSON) -> None:
        self.id = id
        self.timestamp = timestamp
        self.is_fast = is_fast
        self.customer_id = customer_id
        self.products = products

    def __repr__(self) -> str:
        return f'Order {self.id}'


