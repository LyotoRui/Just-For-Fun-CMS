from flask import Flask
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from loguru import logger

from .routes.control_panel import control_panel
from .routes.cp_auth import cp_auth
from .routes.cp_product import cp_product
from .routes.cp_category import cp_category
from .routes.cp_settings import cp_settings

logger.add(
    "debug.log",
    level="ERROR",
    format="{time:HH:mm:ss!UTC} {level} {message}",
    rotation="10 KB",
    compression="zip",
)


def register_blueprints(app: Flask) -> None:
    control_panel.register_blueprint(cp_auth)
    control_panel.register_blueprint(cp_product)
    control_panel.register_blueprint(cp_category)
    control_panel.register_blueprint(cp_settings)
    app.register_blueprint(control_panel, url_prefix="/cp")


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(filename="config.py", silent=False)
    register_blueprints(app=app)
    return app


app = create_app()

db = SQLAlchemy(app=app)

mail = Mail(app=app)

migrate = Migrate(app=app, db=db)
