from sqlalchemy import JSON
from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Float)
    title_image = db.Column(db.String(100))
    is_avaliable = db.Column(db.Boolean, default=False)
    parent_category = db.Column(db.Integer, db.ForeignKey('category.id'))
    description = db.Column(db.JSON)

    def __init__(self, id: int, name: str, price: float, title_image: str, is_avaliable: bool, parent_category: int, description: JSON) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.title_image = title_image
        self.is_avaliable = is_avaliable
        self.parent_category = parent_category
        self.description = description
    
    def __repr__(self) -> str:
        return f'Product {self.id}'

