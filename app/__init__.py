from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

logger.add(
    "debug.log",
    level="ERROR",
    format="{time:HH:mm:ss!UTC} {level} {message}",
    rotation="10 KB",
    compression="zip",
)


def register_blueprints(app: Flask) -> None:
    from .routes.control_panel import control_panel
    from .routes.cp_auth import auth
    control_panel.register_blueprint(auth)
    app.register_blueprint(control_panel)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(filename="config.py", silent=False)
    register_blueprints(app=app)
    return app


def create_db_tables() -> None:
    pass

app = create_app()

db = SQLAlchemy(app=app)

mail = Mail(app=app)

migrate = Migrate(app=app, db=db)
