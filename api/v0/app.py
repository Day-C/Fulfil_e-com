#!/usr/bin/python3
"""Flask app"""
from flask import Flask, render_template
import models
from .views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(e):
    """close session"""

    models.storage.close()


@app.route('/')
def home():
    """test frontend"""

    return render_template('index.html')

@app.route('/admin')
def admin():
    """test adim page"""

    return render_template('admin.html')

@app.route('/login')
def user_login():
    """Render login page."""

    return render_template('login.html')
@app.route('/signup')
def usr_signup():
    """create new user account."""

    return render_template('signup.html')

@app.route('/Fulfil')
def landing_page():
    """ projects landing page"""

    return render_template('landing.html')

@app.route('/about')
def about_page():
    """render about page"""

    return render_template('about.html')


if __name__ == "__main__":
    app.run( debug=True, host="0.0.0.0", port=5000)
