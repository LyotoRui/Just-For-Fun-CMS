from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone = db.Column(db.String(13), nullable=False)

    def __init__(self, id: int, first_name: str, last_name: str, email: str, phone: str) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
    
    def __repr__(self) -> str:
        return f'User {self.id}'
