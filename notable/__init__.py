import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

# Set the secret key
app.config['SECRET_KEY'] = "118d24d0a9c3a6d792d5c484e9cd076f"

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Initialize the database
db = SQLAlchemy(app)

# Initialize the bcrypt
bcrypt = Bcrypt(app)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = 'info'

# Constants for Mail Server
app.config['MAIL_SERVER'] = "smtp.googlemail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)





from notable import routes
