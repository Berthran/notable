from datetime import datetime
from notable import db


class Task(db.Model):
    '''
    Task object.

    A task is a section of a note that represents a task to be done by the user.
    A task can have sub-tasks that are also tasks to be done by the user.
    A task can have guidelines that are benchmarks or instructions to help the user complete the task.


    '''
    id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)
    progress = db.Column(db.Integer, nullable=False, default=0)
    subtasks = db.relationship('Subtask', backref='parent', lazy=True)
    guidelines = db.relationship('Guideline', backref='task', lazy=True)


    def __repr__(self):
        return f'Task [{self.title}] {self.body}>'


    
class Subtask(db.Model):
    '''
    Subtask object.

    A subtask is a task that is part of a task. A subtask is a task that is done to complete the main task.
    A subtask is associated with a task.
    '''
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'Subtask [{self.title}] {self.body}>'


class Guideline(db.Model):
    '''
    Guideline object.

    A guideline is a set of instructions or benchmarks that help the user to complete a task.
    A guideline is associated with a task.

    Basic guidelines that will be available for the user to include in their task are:
    - Define the purpose of the task: WHAT IS THE PURPOSE OF THIS PURPOSE OF THIS TASK?
    - Set a priority for the task (High, Medium, Low): HOW IMPORTANT IS THIS TASK TO YOU?
    - Set a deadline for the task (date and time): HOW LONG DO YOU HAVE TO COMPLETE THIS TASK?
    - Set a category for the task (Work, Personal, Health, Finance, Education, Other): WHAT AREA OF YOUR LIFE DOES PERFORMING THIS TASK IMPACT?
    - Set a status for the task (Not started, In progress, Completed): WHERE ARE YOU IN THE PROCESS OF COMPLETING THIS TASK?
    - Set a reward for completing the task: WHAT WILL YOU GAIN FROM COMPLETING THIS TASK?
    - Set a penalty for not completing the task: WHAT WILL YOU LOSE IF YOU DON'T COMPLETE THIS TASK?
    - Set a location for the task: WHERE DO YOU NEED TO BE TO COMPLETE THIS TASK?
    - Set a budget for the task: HOW MUCH MONEY DO YOU NEED TO COMPLETE THIS TASK?
    - Set a duration for the task: HOW LONG WILL IT TAKE TO COMPLETE THIS TASK?
    - Add a note to the task (additional information about the task after completion or end of the task deadline): WHAT DO YOU NEED TO REMEMBER ABOUT THIS TASK?
    - Add a checklist for the task (a list of items to be done to complete the task): WHAT DO YOU NEED TO DO TO COMPLETE THIS TASK?
    - Add a progress tracker for the task (a percentage of the task done): HOW FAR ALONG ARE YOU IN COMPLETING THIS TASK?
    - Add a timer for the task (a countdown timer to complete the task): HOW MUCH TIME DO YOU HAVE LEFT TO COMPLETE THIS TASK?
    '''
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    key = db.Column(db.String(40), nullable=False)
    value = db.Column(db.String(40), nullable=False)
    purpose = db.Column(db.String(40), nullable=True)
    priority = db.Column(db.String(40), nullable=True)
    deadline = db.Column(db.DateTime, nullable=True)
    category = db.Column(db.String(40), nullable=True)
    status = db.Column(db.String(40), nullable=True)
    reward = db.Column(db.String(40), nullable=True)
    penalty = db.Column(db.String(40), nullable=True)
    location = db.Column(db.String(40), nullable=True)
    budget = db.Column(db.String(40), nullable=True)
    duration = db.Column(db.String(40), nullable=True)
    note = db.Column(db.String(40), nullable=True)



    def __repr__(self):
        return f'Guideline [{self.key}] {self.value}>'

    

