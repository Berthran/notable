import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from notable.models.note import Note
from notable import db, mail

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

def add_demo_notes(user):
    # Add demo notes for new users
    for demoNote in demoNotes:
        note = Note(title=demoNote['title'], body=demoNote['body'], author=user)
        db.session.add(note)
        db.session.commit()

def save_picture(form_picture):
    ''' Save uploaded image to database '''
    # Generate a random string to store file name
    random_hex = secrets.token_hex(8)
    # Get the file extension
    _, f_ext = os.path.splitext(form_picture.filename)
    # Create a custom picture file name
    picture_fn = random_hex + f_ext
    # Get the absolute path to store the picture in
    picture_path =  os.path.join(current_app.root_path, 'static/profile_pics',  picture_fn)
    # Resize picture
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    # Save the picture
    i.save(picture_path)
    return (picture_fn)

def send_reset_email(user):
    ''' Send a token to user '''
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did note make this request then simply ignore this email and no change will be made
'''
    mail.send(msg)