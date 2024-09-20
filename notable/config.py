import os
from notable import app
from flask_mail import Mail

class Config:
    # Set the secret key
    app.config['SECRET_KEY'] = "118d24d0a9c3a6d792d5c484e9cd076f"

    # Set the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    # Constants for Mail Server
    app.config['MAIL_SERVER'] = "smtp.googlemail.com"
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    mail = Mail(app)