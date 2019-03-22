from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
        SECRET_KEY = 'topsecret',
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/catalog_db',
        SQLALCHEMY_TRACK_MOdIFICATIONS=False

db = SQLAlchemy(app)

@app.route('/index')
@app.route('/')
