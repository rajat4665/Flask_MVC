import os
from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(
	__name__,
	template_folder = template_dir,
	static_folder = static_dir
	)

app.config["SECRET_KEY"] = "AGRA_KA_DABRA"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_api.sqlite3'
