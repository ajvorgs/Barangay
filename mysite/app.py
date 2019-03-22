from flask import Flask, render_template, request, session, g
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.update(
        SECRET_KEY = 'topsecret',
        SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/testpython',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
        )

db=SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
