import json
import os
from datetime import datetime


class Task:
    """Model representing a task."""
    
    def __init__(self, title, description="", completed=False):
        self.id = None
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert task to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary."""
        task = cls(data['title'], data.get('description', ''), data.get('completed', False))
        task.id = data.get('id')
        task.created_at = data.get('created_at', datetime.now().isoformat())
        return task


class TaskRepository:
    """Repository for task persistence using JSON file."""
    
    def __init__(self, data_file='data/tasks.json'):
        self.data_file = data_file
        self.tasks = []
        self._load_tasks()
    
    def _load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        else:
            self.tasks = []
    
    def _save_tasks(self):
        """Save tasks to JSON file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=2, ensure_ascii=False)
    
    def add(self, task):
        """Add a new task."""
        # Generate ID
        task.id = len(self.tasks) + 1
        self.tasks.append(task)
        self._save_tasks()
        return task
    
    def get_all(self):
        """Get all tasks."""
        return self.tasks.copy()
    
    def get_by_id(self, task_id):
        """Get task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update(self, task_id, **kwargs):
        """Update task."""
        task = self.get_by_id(task_id)
        if task:
            for key, value in kwargs.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            self._save_tasks()
            return task
        return None
    
    def delete(self, task_id):
        """Delete task."""
        task = self.get_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self._save_tasks()
            return True
        return False
    
    def clear(self):
        """Clear all tasks."""
        self.tasks = []
        self._save_tasks()
