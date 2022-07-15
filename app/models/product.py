from app import db
from sqlalchemy.dialects.postgresql import JSON


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    title_image = db.Column(db.String(50), nullable=False)
    short_desc = db.Column(db.String(150))
    full_desc = db.Column(db.Text)
    meta = db.Column(db.String(150))
    specs = db.Column(JSON)