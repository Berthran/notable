from flask import render_template, request, Blueprint
from notable.models.note import Note
from flask_login import current_user, login_required


main = Blueprint('main', __name__)



@main.route('/', strict_slashes=False)
@main.route('/home', strict_slashes=False)
@login_required
def home():
    ''' Shows the homepage '''
    # Get notes created by the user
    # if current_user.is_authenticated:
    #     notes = Note.query.filter_by(user_id=current_user.id)
    # else:
    #     notes = demoNotes
    page = request.args.get('page', 1, type=int)
    notes = Note.query.filter_by(author=current_user)\
        .order_by(Note.created_at.desc())\
        .paginate(page=page, per_page=5)
    return render_template('home.html', notes=notes, title="Home")


# @main.route('/notes', strict_slashes=False)
# def notes():
#     ''' Handles all notes '''
#     return 'All Notes page'


@main.route('/note/<int:note_id>/report', strict_slashes=False)
def note_report(note_id):
    ''' Handles note report '''
    page = request.args.get('page', 1, type=int)
    notes = Note.query.filter_by(author=current_user)\
        .order_by(Note.created_at.desc())\
        .paginate(page=page, per_page=5)
    return render_template('note_report.html', notes=notes)
