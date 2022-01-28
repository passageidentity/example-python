from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # blueprint for auth routes in our app
    from .main import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return app


