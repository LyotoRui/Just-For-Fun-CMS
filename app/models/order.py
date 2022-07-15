from datetime import datetime
from app import db
from sqlalchemy.dialects.postgresql import JSON

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key = True)
    customers_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    goods = db.Column(JSON)