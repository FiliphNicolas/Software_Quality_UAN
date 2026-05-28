class Storage:
    def __init__(self):
        self.tasks = []
    
    def save(self, task):
        """Save a task to storage."""
        if not task or not task.get('title'):
            raise ValueError("Task must have a title")
        
        # Check for duplicate tasks
        for existing_task in self.tasks:
            if existing_task.get('title') == task.get('title'):
                raise ValueError("Task with this title already exists")
        
        self.tasks.append(task)
        return True
    
    def get_all(self):
        """Retrieve all tasks from storage."""
        return self.tasks.copy()
    
    def clear(self):
        """Clear all tasks from storage."""
        self.tasks = []
