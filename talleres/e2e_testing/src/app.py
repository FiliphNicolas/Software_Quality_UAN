from flask import Flask, render_template, request, redirect, url_for
from models import TaskRepository

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'

# Initialize repository
repo = TaskRepository()


@app.route('/')
def index():
    """Home page - list all tasks."""
    tasks = repo.get_all()
    return render_template('index.html', tasks=tasks)


@app.route('/create', methods=['POST'])
def create_task():
    """Create a new task."""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    
    if title:
        task = repo.add(Task(title, description))
    
    return redirect(url_for('index'))


@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Mark a task as completed."""
    repo.update(task_id, completed=True)
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task."""
    repo.delete(task_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
