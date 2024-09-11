'''
Handles the different component routes
'''
import os
import secrets
from PIL import Image
from flask import Flask, render_template, flash, redirect, url_for, request
from notable.forms import RegistrationForm, LoginForm, NoteForm, UpdateAccountForm
from notable import app, db, bcrypt
from notable.models import User, Note
from flask_login import login_user, current_user, logout_user, login_required

demoNotes = [
    {
        'id': 1,
        'title': 'Demo Note 1',
        'body': "I decree by the word of the Lord that I am no debtor to the flesh to walk after the flesh. Body you are not my master neither am I your slave therefore by the Spirit of the Lord I decree your deeds mortified and destroyed in me. (Rom 8:12,13). \nHave mercy on me oh Lord and bring to a halt every activity distracting me from the path you want me to follow.",
        'date_posted': 'April 20, 2021'
    },
    {
        'id': 2,
        'title': 'Demo Note 2',
        'body': 'This is the second note',
        'date_posted': 'April 21, 2021'
    }
]

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    ''' Shows the homepage '''
    # Get notes created by the user
    if current_user.is_authenticated:
        notes = Note.query.filter_by(user_id=current_user.id)
    else:
        notes = demoNotes
    return render_template('home.html', allNotes=notes, title="Home")


def add_demo_notes(user):
    # Add demo notes for new users
    for demoNote in demoNotes:
        note = Note(title=demoNote['title'], body=demoNote['body'], author=user)
        db.session.add(note)
        db.session.commit()


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    ''' Handles user registration '''
    # Create an instance of the registration form
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstName.data,
                lastname=form.lastName.data,
                email=form.email.data,
                password=hashed_password)
        db.session.add(user)
        db.session.commit()
        add_demo_notes(user)
        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)
    


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    ''' Handles user login '''
    # Create an instance of the login form

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Check email and password', 'danger')
    return render_template('login.html', title="Login", form=form)


@app.route('/logout', strict_slashes=False)
def logout():
    ''' Handles user logout '''
    logout_user()
    return redirect(url_for('home'))



def save_picture(form_picture):
    ''' Save uploaded image to database '''
    # Generate a random string to store file name
    random_hex = secrets.token_hex(8)
    # Get the file extension
    _, f_ext = os.path.splitext(form_picture.filename)
    # Create a custom picture file name
    picture_fn = random_hex + f_ext
    # Get the absolute path to store the picture in
    picture_path =  os.path.join(app.root_path, 'static/profile_pics',  picture_fn)
    # Resize picture
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # Save the picture
    i.save(picture_path)
    return (picture_fn)
    


@app.route('/account', methods=['GET', 'POST'], strict_slashes=False)
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.firstName.data = current_user.firstname
        form.lastName.data = current_user.lastname
        form.email.data = current_user.email
    image_file = url_for('static', filename=f'/profile_pics/{current_user.image}')
    return render_template('account.html', title="Account", image_file=image_file, form=form)


@app.route('/notes', strict_slashes=False)
def notes():
    ''' Handles all notes '''
    return 'All Notes page'


@app.route('/note/new', methods=['GET', 'POST'], strict_slashes=False) # For the create note button
@login_required
def new_note():
    ''' Handles new note creation '''
    form = NoteForm()

    if form.validate_on_submit():
        note = Note(title=form.title.data,
                    body=form.content.data,
                    author=current_user)
        db.session.add(note)
        db.session.commit()
        flash('Note created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_note.html', title='New Post', form=form)

@app.route('/note/<int:note_id>/<int:task_id>/guidelines', strict_slashes=False)
def guidelines(note_id, task_id):
    ''' Handles the guidelines view'''
    return ' Guideline Page'

# No automatic editing on viewing a note
@app.route('/note/<int:note_id>', strict_slashes=False) # Tap on note to view. Disables automatic edit
def view_note(note_id):
    ''' Handles note view '''
    return 'View Note page'


@app.route('/note/<int:note_id>/edit', strict_slashes=False) # Click on edit icon
def edit_note(note_id):
    ''' Handles note edit '''
    return 'Edit Note page'


@app.route('/note/<int:note_id>/delete', strict_slashes=False)
def delete_note(note_id):
    ''' Handles note delete '''
    return 'Delete Note page'


@app.route('/note/<int:note_id>/report', strict_slashes=False)
def report_note(note_id):
    ''' Handles note report '''
    return 'Report Note page'


@app.route('/reports', strict_slashes=False)
def reports():
    ''' Handles all reports '''
    return 'All Reports page'

@app.route('/report/<int:report_id>', strict_slashes=False)
def view_report(report_id):
    ''' Handles report view '''
    return 'View Report page'

@app.route('/report/<int:report_id>/edit', strict_slashes=False)
def edit_report(report_id):
    ''' Handles report edit '''
    return 'Edit Report page'

@app.route('/report/<int:report_id>/delete', strict_slashes=False)
def delete_report(report_id):
    ''' Handles report delete '''
    return 'Delete Report page'


# @app.route('/profile/delete', strict_slashes=False)
# def delete_profile():
#     ''' Handles user profile delete '''
#     return 'Delete Profile page'

# @app.route('/profile/change-password', strict_slashes=False)
# def change_password():
#     ''' Handles user password change '''
#     return 'Change Password page'

# @app.route('/profile/forgot-password', strict_slashes=False)
# def forgot_password():
#     ''' Handles user forgot password '''
#     return 'Forgot Password page'

# @app.route('/profile/reset-password', strict_slashes=False)
# def reset_password():
#     ''' Handles user reset password '''
#     return 'Reset Password page'

# @app.route('/profile/notifications', strict_slashes=False)
# def notifications():
#     ''' Handles user notifications '''
#     return 'Notifications page'
