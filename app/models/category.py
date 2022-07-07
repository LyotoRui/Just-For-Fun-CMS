from sqlalchemy import JSON
from app import db

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    title_image = db.Column(db.String(100))
    is_avaliable = db.Column(db.Boolean, default=False)
    description = db.Column(db.JSON)

    def __init__(self, id: int, name: str, title_image: str, is_avaliable: bool, description: JSON) -> None:
        self.id = id
        self.name = name
        self.title_image = title_image
        self.is_avaliable = is_avaliable
        self.description = description
    
    def __repr__(self) -> str:
        return f'Category {self.id}'