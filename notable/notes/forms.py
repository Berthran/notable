from flask_wtf import FlaskForm #type: ignore
from wtforms import StringField, TextAreaField, SubmitField # type: ignore
from wtforms.validators import DataRequired # type: ignore


class NoteForm(FlaskForm):
    '''
    Form for creating new notes
    '''
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content") # A user can create an empty note
    save = SubmitField('Save')