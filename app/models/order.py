from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key = True)
    customers_id = db.Column(db.Integer)
    status_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    goods = db.Column(JSON)
    payment_method = db.Column(db.Integer, nullable=False)
    delivery_type = db.Column(db.Integer, nullable=False)
    address = db.Column(JSON)

    def __init__(self, customers_id: int, status_id: int, goods: JSON, payment_method: int, delivery_type: int, addrress: int) -> None:
        self.customers_id = customers_id
        self.status_id = status_id
        self.goods = goods
        self.payment_method = payment_method
        self.delivery_type = delivery_type
        self.address = addrress