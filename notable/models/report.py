from datetime import datetime
from notable import db



class Report(db.Model):
    '''
    Report object.

    At the end of the day, the user can generate a report of the tasks done and the tasks not done.
    The report will show the user the progress made in completing their tasks.
    The report will show the user the tasks that are done and the tasks that are not done.
    The report will contain a summary of the user's progress for the day using a task completion percentage calculated
    for all tasks and subtasks for a given note in the user's account.

    A report is associated with a note.
    '''
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    note_title = db.Column(db.String(40), nullable=False)
    task_title = db.Column(db.String(40), nullable=False)
    task_completion_score = db.Column(db.Integer, nullable=False)
    overall_completion_Score = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'Report [{self.done}] {self.notDone}>'
