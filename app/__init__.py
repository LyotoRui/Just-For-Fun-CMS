from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

from .commands import create_db, create_su

from .routes.control_panel import control_panel
from .routes.cp_auth import auth

logger.add(
    "debug.log",
    level="ERROR",
    format="{time:HH:mm:ss!UTC} {level} {message}",
    rotation="10 KB",
    compression="zip",
)

def register_blueprints(app: Flask) -> None:
    control_panel.register_blueprint(auth)
    app.register_blueprint(control_panel)


def register_commands(app: Flask) -> None:
    app.cli.add_command(create_db)
    app.cli.add_command(create_su)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(filename="config.py", silent=False)
    register_commands(app=app)
    register_blueprints(app=app)
    
    return app


app = create_app()

db = SQLAlchemy(app=app)

mail = Mail(app=app)
