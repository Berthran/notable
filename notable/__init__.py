from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from notable.config import Config

app = Flask(__name__)

# Configure the app
app.config.from_object(Config)

# Initialize the database
db = SQLAlchemy(app)

# Initialize the bcrypt
bcrypt = Bcrypt(app)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = 'info'

# Initialize the mail server
mail = Mail(app)


from notable.users.routes import users
from notable.notes.routes import notes
from notable.main.routes import main

app.register_blueprint(users)
app.register_blueprint(notes)
app.register_blueprint(main)