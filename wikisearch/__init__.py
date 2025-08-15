from flask import Flask
from typing import Any
from flask_cors import CORS
from .search import search_bp
from .summarize import summarize_bp

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.register_blueprint(search_bp)
    app.register_blueprint(summarize_bp)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    return app