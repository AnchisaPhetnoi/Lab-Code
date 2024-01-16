from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(200), nullable=False)
    task_master = db.Column(db.String(50), nullable=False)
    task_responsible = db.Column(db.String(50), nullable=False)
    task_due_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_name = request.form['task_name']
        task_master = request.form['task_master']
        task_responsible = request.form['task_responsible']
        task_due_date = datetime.strptime(request.form['task_due_date'], '%Y-%m-%d')

        new_task = Todo(task_name=task_name, task_master=task_master, task_responsible=task_responsible, task_due_date=task_due_date)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.task_due_date).all()
        return render_template('main.html', tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
