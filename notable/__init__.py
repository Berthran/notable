from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from notable.config import Config


# Initialize the database
db = SQLAlchemy()

# Initialize the bcrypt
bcrypt = Bcrypt()

# Initialize the login manager
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = 'info'

# Initialize the mail server
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    # Configure the app
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from notable.users.routes import users
    from notable.notes.routes import notes
    from notable.main.routes import main
    from notable.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(notes)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return (app)
