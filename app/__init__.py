from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

logger.add('debug.log', level='ERROR', format='{time:HH:mm:ss!UTC} {level} {message}', rotation='10 KB', compression='zip')


def register_blueprints(app: Flask) -> None:
    pass

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(filename='config.py', silent=False)
    register_blueprints(app=app)
    return app

def init_mail(app: Flask) -> Mail:
    return Mail(app=app)

def init_db(app: Flask) -> SQLAlchemy:
    return SQLAlchemy(app=app)

def init_migrate(app: Flask, db: SQLAlchemy) -> Migrate:
    return Migrate(app=app, db=db)