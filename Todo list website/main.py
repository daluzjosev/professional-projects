from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todolist.db'
db = SQLAlchemy(app)

class Quests(db.Model):
    __tablename__ = "Quests"
    id = db.Column(db.Integer, primary_key=True)

    quest = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/', methods=["GET","POST"])
def todos():
    if request.method == 'POST':
        text = request.form['todo-input']
        new_item = Quests(quest=text)
        db.session.add(new_item)
        db.session.commit()        
    todos = Quests.query.all()
    return render_template("index.html", todos=todos)

if __name__ == "__main__":
    with app.app_context():
        # db.create_all()
        app.run(host='0.0.0.0', port=5000, debug=True)
