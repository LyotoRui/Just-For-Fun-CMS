from flask import Flask
from loguru import logger

logger.add('debug.log', level='ERROR', format='{time:HH:mm:ss!UTC} {level} {message}', rotation='10 KB', compression='zip')

def init() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    return app
