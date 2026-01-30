"""
Python fact: (this is not Flask-specific)
If a folder has __init__.py, Python treats it as a package, not just a directory.
"""
from flask import Flask

# function to link Flask object, its methods, and main.py driver file
def create_app() -> Flask:
    app = Flask(__name__) # create Flask object instance called "app"
    from .routes import main # imports Flask blueprint for "app" from main.py
    app.register_blueprint(main) # gives "app" access to routes from "main" blueprint
    return app