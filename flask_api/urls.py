
from flask_api.settings import *
from flask import redirect , render_template, url_for
from flask_api.views import home_view , login_view , register_view

@app.route('/')
def home():
    return home_view()

@app.route('/login/')
def login():
    return login_view()

@app.route('/register/')
def register():
    return register_view()
