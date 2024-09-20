from datetime import datetime
from notable import db
from notable.models.task import Task
from notable.models.report import Report


class Note(db.Model):
    '''
    A note object.

    A note is a section of text and/or tasks created by a user. A note has a title and a body.
    The body of a note can contain text and/or tasks.
    A note is related to a user who created it by the user's userId.

    Where there are tasks in a note, the tasks are displayed in the note's body as a list of tasks with
    a checkbox to indicate if the task is done or not. A task can have sub-tasks which are also displayed
    in the note's body. A task with sub-tasks has a progress tracker indicator. The progress tracker
    indicates the percentage of sub-tasks that are done. The progress tracker is calculated as the
    number of sub-tasks done divided by the total number of sub-tasks in the task. The progress tracker
    is displayed as a percentage.

    Each task can be given a set of guidelines or benchmarks that will help the user to stay on track to
    complete the task. 
    By default, a task has no guidelines. However, the user can add guidelines to a task by clicking on the guideline icon represented by three dots 
    positioned on the far right of the task.

    The guidelines when added remain hidden until the user clicks on the guideline icon to view them.
    '''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tasks = db.relationship('Task', backref='owner', lazy=True)
    reports = db.relationship('Report', backref='owner', lazy=True)


    def __repr__(self):
        return f'[{self.title}]: {self.created_at}\n'