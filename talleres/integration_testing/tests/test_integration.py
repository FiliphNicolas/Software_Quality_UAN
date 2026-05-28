import pytest
from src.service import Service
from src.storage import Storage
from src.notifier import Notifier


class TestIntegration:
    """Initial integration tests - deliberately incomplete."""
    
    def test_add_task_basic(self):
        """Test basic task addition."""
        service = Service()
        result = service.add_task("Test task", "Test description")
        assert result is True
    
    def test_get_tasks(self):
        """Test retrieving tasks."""
        service = Service()
        service.add_task("Task 1")
        tasks = service.get_tasks()
        assert len(tasks) > 0
    
    def test_notification_sent(self):
        """Test that notification is sent when task is added."""
        service = Service()
        service.add_task("Task 1")
        notifications = service.get_notifications()
        assert len(notifications) > 0
