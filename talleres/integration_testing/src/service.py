from .storage import Storage
from .notifier import Notifier


class Service:
    def __init__(self, storage=None, notifier=None):
        self.storage = storage or Storage()
        self.notifier = notifier or Notifier()
    
    def add_task(self, title, description=""):
        """
        Add a new task to the system.
        
        This method integrates with Storage and Notifier to:
        1. Store the task
        2. Send a notification about the new task
        
        Returns:
            bool: True if the task was added successfully, False otherwise.
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        task = {
            'title': title.strip(),
            'description': description.strip()
        }
        
        # Try to save the task
        try:
            self.storage.save(task)
        except Exception as e:
            # If storage fails, don't proceed with notification
            raise e
        
        # Try to send notification
        try:
            self.notifier.send(f"New task added: {title}")
        except Exception as e:
            # If notification fails, we should still consider the task added
            # but log the error (in a real system)
            print(f"Notification failed: {e}")
        
        return True
    
    def get_tasks(self):
        """Retrieve all tasks."""
        return self.storage.get_all()
    
    def get_notifications(self):
        """Retrieve all notifications."""
        return self.notifier.get_notifications()
