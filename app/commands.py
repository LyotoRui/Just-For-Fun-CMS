import click
from flask.cli import with_appcontext
from getpass import getpass
from werkzeug.security import generate_password_hash
from loguru import logger

@click.command(name='create-db')
@with_appcontext
def create_db() -> None:
    try:
        from . import db
        from .models.customer import Customer
        from .models.order import Order
        from .models.product import Product
        from .models.user import User
        db.create_all()
        logger.info('Models created successfully')
    except Exception as error:
        logger.error(error)
    

@click.command(name='create-su')
@with_appcontext
def create_su() -> None:
    from .models.user import User, UserRole
    from . import db
    try:
        su = User(
            login=str(input('Login: ')),
            password=generate_password_hash(str(getpass('Password: '))),
            email=str(input('Email: ')),
            first_name=str(input('First name: ')),
            last_name=str(input('Last name: ')),
            role=UserRole.SUPER_USER
        )
        db.session.add(su)
        db.session.commit()
    except Exception as error:
        logger.error(error)