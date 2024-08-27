'''
Handles the different component routes
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def homepage():
    ''' Shows the homepage '''
    return ('Home Page')


@app.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def registration():
    ''' Handles user registration '''
    # return render_template('registration.html')
    return 'Registration page'


@app.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    ''' Handles user login '''
    # return render_template('login.html')
    return 'Login page'


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


@app.route('/new_note', strict_slashes=False)
def new_note():
    ''' Handles new note creation '''
    return 'New Note page'


@app.route('/note/<int:note_id>', strict_slashes=False)
def view_note(note_id):
    ''' Handles note view '''
    return 'View Note page'


@app.route('/note/<int:note_id>/edit', strict_slashes=False)
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



if __name__ == "__main__":
    app.run(debug=True, port=5000,
            host='0.0.0.0',
            threaded=True,
            use_reloader=True,
            use_debugger=True)
