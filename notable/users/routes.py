from flask import render_template, flash, redirect, url_for, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from notable import db, bcrypt
from notable.models.user import User
from notable.models.note import Note
from notable.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm,
                                 RequestResetForm, ResetPasswordForm)
from notable.users.utils import  add_demo_notes, save_picture, send_reset_email


users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    ''' Handles user registration '''
    # Create an instance of the registration form
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstName.data,
                lastname=form.lastName.data,
                email=form.email.data.lower(),
                password=hashed_password)
        db.session.add(user)
        db.session.commit()
        add_demo_notes(user)
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title="Register", form=form)
    

@users.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    ''' Handles user login '''
    # Create an instance of the login form

    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@users.route('/logout', strict_slashes=False)
def logout():
    ''' Handles user logout '''
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'], strict_slashes=False)
@login_required
def account():
    ''' Handles user profile '''
    form = UpdateAccountForm()

    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image = picture_file

        current_user.firstname = form.firstName.data
        current_user.lastname = form.lastName.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f'Changes updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.firstName.data = current_user.firstname
        form.lastName.data = current_user.lastname
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'/profile_pics/{current_user.image}')
    return render_template('account.html', title="Account", image_file=image_file, form=form)


@users.route('/reset_password', methods= ['GET', 'POST'], strict_slashes=False)
def reset_request():
    ''' Handles requesting for password reset '''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        # Send email to user with the token
        send_reset_email(user)
        flash(f"An email has been sent to {user.email}. Kindly follow\
              the instructions to reset your password", "info")
        return redirect(url_for('users.login'))

    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password', methods= ['GET', 'POST'], strict_slashes=False)
def reset_token(token):
    ''' Handles password reset '''
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    user = User.verify_reset_token(token)
    if user is None:
        flash('Token is invalid or expired', 'warning')
        return redirect(url_for('users.reset_request'))
    
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        add_demo_notes(user)
        flash(f'Your password has been changed successfully!!!', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
