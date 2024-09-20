from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(404)
def error_404(error):
    '''
    Handles 404 error
    '''
    return render_template('errors/404.html'), 404

@errors.app_errorhandler(403)
def error_403(error):
    '''
    Handles 403 error
    '''
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(405)
def error_405(error):
    '''
    Handles 405 error
    '''
    return render_template('errors/405.html'), 405

@errors.app_errorhandler(500)
def error_500(error):
    '''
    Handles 500 error
    '''
    return render_template('errors/500.html'), 500
