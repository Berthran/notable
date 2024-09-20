from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from flask_login import current_user
from notable.models.user import User

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
    

class UpdateAccountForm(FlaskForm):
    '''
    Form for updating user profile
    '''
    firstName = StringField('First name', validators=[DataRequired(), Length(min=2, max=20)])
    lastName = StringField('Last name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')


    # Validatate the email
    def validate_email(self, email):
        '''
        Validates the user provided email
        '''
        # Email must be unique
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('An account witht this email already exists. Login or use a different email.')
            

class RequestResetForm(FlaskForm):
    '''
    Handles password reset request
    '''
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

     # Validatate the user account exists
    def validate_email(self, email):
        '''
        Validates the user provided email
        '''
        # Check if the email already exists
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first')
    

class ResetPasswordForm(FlaskForm):
    '''
    Handles password reset
    '''
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')