"""
Bottom-Up Integration Tests using Drivers.

These tests test the lower-level modules (Storage and Notifier) in isolation
using drivers to provide input and verify output before higher-level modules
are fully implemented.
"""
import pytest
from src.storage import Storage
from src.notifier import Notifier


class StorageDriver:
    """Driver to test Storage module in isolation."""
    
    def __init__(self):
        self.storage = Storage()
    
    def test_save_valid_task(self):
        """Test saving a valid task."""
        task = {'title': 'Valid Task', 'description': 'Test'}
        result = self.storage.save(task)
        return result
    
    def test_save_empty_title(self):
        """Test saving a task with empty title."""
        try:
            task = {'title': '', 'description': 'Test'}
            self.storage.save(task)
            return False  # Should have raised an error
        except ValueError:
            return True  # Correctly raised an error
    
    def test_save_none_title(self):
        """Test saving a task with None title."""
        try:
            task = {'title': None, 'description': 'Test'}
            self.storage.save(task)
            return False  # Should have raised an error
        except ValueError:
            return True  # Correctly raised an error
    
    def test_save_duplicate_task(self):
        """Test saving a duplicate task."""
        task = {'title': 'Duplicate', 'description': 'Test'}
        self.storage.save(task)
        try:
            self.storage.save(task)  # Try to save again
            return False  # Should have raised an error
        except ValueError:
            return True  # Correctly raised an error
    
    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        self.storage.clear()
        self.storage.save({'title': 'Task 1', 'description': 'Test'})
        self.storage.save({'title': 'Task 2', 'description': 'Test'})
        return self.storage.get_all()
    
    def test_clear_tasks(self):
        """Test clearing all tasks."""
        self.storage.save({'title': 'Task 1', 'description': 'Test'})
        self.storage.clear()
        return len(self.storage.get_all()) == 0


class NotifierDriver:
    """Driver to test Notifier module in isolation."""
    
    def __init__(self):
        self.notifier = Notifier()
    
    def test_send_valid_message(self):
        """Test sending a valid message."""
        result = self.notifier.send("Test message")
        return result
    
    def test_send_empty_message(self):
        """Test sending an empty message."""
        try:
            self.notifier.send("")
            return False  # Should have raised an error
        except ValueError:
            return True  # Correctly raised an error
    
    def test_send_none_message(self):
        """Test sending a None message."""
        try:
            self.notifier.send(None)
            return False  # Should have raised an error
        except ValueError:
            return True  # Correctly raised an error
    
    def test_get_notifications(self):
        """Test retrieving all notifications."""
        self.notifier.clear()
        self.notifier.send("Message 1")
        self.notifier.send("Message 2")
        return self.notifier.get_notifications()
    
    def test_clear_notifications(self):
        """Test clearing all notifications."""
        self.notifier.send("Test message")
        self.notifier.clear()
        return len(self.notifier.get_notifications()) == 0


class TestBottomUpStorage:
    """Bottom-Up integration tests for Storage module."""
    
    def test_storage_save_valid_task(self):
        """Test that Storage can save a valid task."""
        driver = StorageDriver()
        result = driver.test_save_valid_task()
        assert result is True
    
    def test_storage_rejects_empty_title(self):
        """Test that Storage rejects tasks with empty titles."""
        driver = StorageDriver()
        result = driver.test_save_empty_title()
        assert result is True
    
    def test_storage_rejects_none_title(self):
        """Test that Storage rejects tasks with None titles."""
        driver = StorageDriver()
        result = driver.test_save_none_title()
        assert result is True
    
    def test_storage_rejects_duplicate_tasks(self):
        """Test that Storage rejects duplicate tasks."""
        driver = StorageDriver()
        result = driver.test_save_duplicate_task()
        assert result is True
    
    def test_storage_get_all_returns_all_tasks(self):
        """Test that get_all returns all saved tasks."""
        driver = StorageDriver()
        tasks = driver.test_get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0]['title'] == 'Task 1'
        assert tasks[1]['title'] == 'Task 2'
    
    def test_storage_clear_removes_all_tasks(self):
        """Test that clear removes all tasks."""
        driver = StorageDriver()
        result = driver.test_clear_tasks()
        assert result is True
    
    def test_storage_isolation(self):
        """Test that Storage instances are isolated."""
        storage1 = Storage()
        storage2 = Storage()
        
        storage1.save({'title': 'Task 1', 'description': 'Test'})
        storage2.save({'title': 'Task 2', 'description': 'Test'})
        
        assert len(storage1.get_all()) == 1
        assert len(storage2.get_all()) == 1
        assert storage1.get_all()[0]['title'] == 'Task 1'
        assert storage2.get_all()[0]['title'] == 'Task 2'


class TestBottomUpNotifier:
    """Bottom-Up integration tests for Notifier module."""
    
    def test_notifier_send_valid_message(self):
        """Test that Notifier can send a valid message."""
        driver = NotifierDriver()
        result = driver.test_send_valid_message()
        assert result is True
    
    def test_notifier_rejects_empty_message(self):
        """Test that Notifier rejects empty messages."""
        driver = NotifierDriver()
        result = driver.test_send_empty_message()
        assert result is True
    
    def test_notifier_rejects_none_message(self):
        """Test that Notifier rejects None messages."""
        driver = NotifierDriver()
        result = driver.test_send_none_message()
        assert result is True
    
    def test_notifier_get_all_returns_all_notifications(self):
        """Test that get_notifications returns all sent notifications."""
        driver = NotifierDriver()
        notifications = driver.test_get_notifications()
        assert len(notifications) == 2
        assert notifications[0] == 'Message 1'
        assert notifications[1] == 'Message 2'
    
    def test_notifier_clear_removes_all_notifications(self):
        """Test that clear removes all notifications."""
        driver = NotifierDriver()
        result = driver.test_clear_notifications()
        assert result is True
    
    def test_notifier_isolation(self):
        """Test that Notifier instances are isolated."""
        notifier1 = Notifier()
        notifier2 = Notifier()
        
        notifier1.send("Message 1")
        notifier2.send("Message 2")
        
        assert len(notifier1.get_notifications()) == 1
        assert len(notifier2.get_notifications()) == 1
        assert notifier1.get_notifications()[0] == 'Message 1'
        assert notifier2.get_notifications()[0] == 'Message 2'
