from flask import Blueprint, render_template

error_pages = Blueprint('error_pasges', __name__)

"""
it is not just a basic routing because we don't know what the user is going to provide for errors
therefore, using errorhandler() to connect it to a general error
this is a main approach for setting up your own templates to be served
"""
# We want errorhandler works entire app, so use app_errorhandler
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404

@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 403

