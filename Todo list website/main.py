from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todolist.db'
db = SQLAlchemy(app)

class quests(db.Model):
    __tablename__ = "quests"
    id = db.Column(db.Integer, primary_key=True)

    quest = db.Column(db.String, nullable=False)

@app.route("/")
def add_quest():


if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        app.run(host='0.0.0.0', port=5000, debug=True)
