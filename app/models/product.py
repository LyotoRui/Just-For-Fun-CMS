from app import db
from sqlalchemy.dialects.postgresql import JSON


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    is_avaliable = db.Column(db.Boolean, default=True)
    title_image = db.Column(db.String(50), nullable=False)
    short_desc = db.Column(db.String(150))
    full_desc = db.Column(db.Text)
    meta = db.Column(db.String(150))
    specs = db.Column(JSON)

    def __init__(self, id: int, name: str, is_avaliable: bool, title_image: str, short_desc: str, full_desc: str, meta: str, specs: JSON) -> None:
        self.id = id
        self.name = name
        self.is_avaliable = is_avaliable
        self.title_image = title_image
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.meta = meta
        self.specs = specs
