class Notifier:
    def __init__(self):
        self.notifications = []
    
    def send(self, message):
        """Send a notification."""
        if not message:
            raise ValueError("Message cannot be empty")
        
        self.notifications.append(message)
        return True
    
    def get_notifications(self):
        """Retrieve all sent notifications."""
        return self.notifications.copy()
    
    def clear(self):
        """Clear all notifications."""
        self.notifications = []
