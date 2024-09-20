from datetime import datetime
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from notable import db
from notable.models.note import Note
from notable.notes.forms import NoteForm

notes = Blueprint('notes', __name__)

@notes.route('/note/new', methods=['GET', 'POST'], strict_slashes=False) # For the create note button
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
        # flash('Note created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_note.html', title='New Note',
                           form=form, legend='New Note')


@notes.route('/note/<int:note_id>', strict_slashes=False) # Tap on note title to view. Disables automatic edit
def view_note(note_id):
    ''' Handles note view '''
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    return render_template('note.html', title=note.title, note=note)


@notes.route('/note/<int:note_id>/edit', methods= ['GET', 'POST'], strict_slashes=False) # Click on edit icon
@login_required
def edit_note(note_id):
    ''' Handles note edit '''
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    
    form = NoteForm()
    if form.validate_on_submit():
        note.title = form.title.data
        note.body = form.content.data
        note.updated_at = datetime.utcnow()
        db.session.commit()
        return redirect(url_for('notes.view_note', note_id=note.id))
    elif request.method == 'GET':
        form.title.data = note.title
        form.content.data = note.body
    return render_template('create_note.html', title='Edit Note',
                           form=form, legend="Update Note")


@notes.route('/note/<int:note_id>/delete', methods= ['POST'], strict_slashes=False)
@login_required
def delete_note(note_id):
    ''' Handles note delete '''
    note = Note.query.get_or_404(note_id)
    if note.author != current_user:
        abort(403)
    db.session.delete(note)
    db.session.commit()
    flash(f"Successfully deleted!", 'success')
    return redirect(url_for('main.home'))
