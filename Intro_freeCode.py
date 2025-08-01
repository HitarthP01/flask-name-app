from flask import Flask, render_template, url_for, request, redirect
"""
Flask is the main class used to create a Flask application instance.

render_template is a function used to render (display) HTML files stored 
in a templates folder.
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
"""
A Flask app is a Python program that acts as a web server and web framework.

It listens to HTTP requests (like visiting a URL), and responds with HTML pages, data, or other content.

This app object knows how to:

Register routes (URLs)

Handle requests

Return responses (HTML, JSON, etc.)

Run a local web server for development
"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(150), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # ✅ Correct

    def __repr__(self):
        return '<Task %r>' % self.id
        # return f"<User {self.username}>"



@app.route('/', methods=['POST','GET']) # HTTPs methods for sending and fetching the data from the server.
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "there was an issue adding your task"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

    
"""
def index():
    ...
index = app.route('/')(index)    :---Passing your function (index) into app.route('/')

And it returns a new version of index with routing behavior

"""
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem in deleting"
    
@app.route('/update/<int:id>' , methods = ['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "Update not sucessfull"

    else:
        return render_template('update.html',task=task)


if __name__ == "__main__":
    app.run(debug=True)