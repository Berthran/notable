'''
Handle the forms for registration, login, and new note creation.
'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from notable.models import User


class RegistrationForm(FlaskForm):
    '''
    Form for user registration
    '''
    firstName = StringField('First name', validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    # Validatate the email
    def validate_email(self, email):
        '''
        Validates the user provided email
        '''
        # Check if the email already exists
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('An account witht this email already exists. Login or use a different email.')
        


class LoginForm(FlaskForm):
    '''
    Form for user login
    '''
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class NoteForm(FlaskForm):
    '''
    Form for creating new notes
    '''
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content") # A user can create an empty note
    save = SubmitField('Save')
    

    


