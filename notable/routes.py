'''
Handles the different component routes
'''
from flask import Flask, render_template
from notable.forms import RegistrationForm, LoginForm, NoteForm
from notable import app

allNotes = [
    {
        'id': 1,
        'title': 'First Note',
        'content': 'This is the first note',
        'date_posted': 'April 20, 2021'
    },
    {
        'id': 2,
        'title': 'Second Note',
        'content': 'This is the second note',
        'date_posted': 'April 21, 2021'
    },
    {
        'id': 3,
        'title': 'Third Note',
        'content': 'This is the third note',
        'date_posted': 'April 22, 2021'
    }
]

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    ''' Shows the homepage '''
    return render_template('home.html', allNotes=allNotes, title="Home")
    # return 'Home page'


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    ''' Handles user registration '''
    # Create an instance of the registration form
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)
    


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    ''' Handles user login '''
    # Create an instance of the login form
    form = LoginForm()
    return render_template('login.html')


@app.route('/logout', strict_slashes=False)
def logout():
    ''' Handles user logout '''
    return 'Logout page'


@app.route('/profile', strict_slashes=False)
def profile():
    ''' Handles user profile '''
    return 'Profile page'


@app.route('/notes', strict_slashes=False)
def notes():
    ''' Handles all notes '''
    return 'All Notes page'


@app.route('/new_note', strict_slashes=False) # For the create note button
def new_note():
    ''' Handles new note creation '''
    return 'New Note page'

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


# @app.note('/profile/edit', strict_slashes=False)
# def edit_profile():
#     ''' Handles user profile edit '''
#     return 'Edit Profile page'

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
