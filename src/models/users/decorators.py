from functools import wraps
from src.app import app
from flask import session, render_template


def requires_login(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return render_template("users/requires_login_page.html")
        return func(*args, **kwargs)  #func(...) args: func(5,6), kwargs: func(x=5, y=6)
    return decorated_function

def requires_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' not in session.keys() or session['email'] is None:
            return render_template("users/requires_login_page.html")
        if session['email'] not in app.config['ADMINS']:
            return render_template("users/requires_admin_page.html")
        return func(*args, **kwargs)  #func(...) args: func(5,6), kwargs: func(x=5, y=6)
    return decorated_function


def already_logged_in(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'email' in session.keys() and session['email'] is not None :
            return render_template("users/already_logged_in_page.html")
        return func(*args, **kwargs)  #func(...) args: func(5,6), kwargs: func(x=5, y=6)
    return decorated_function
