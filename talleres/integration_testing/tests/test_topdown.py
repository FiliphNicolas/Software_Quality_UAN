"""
Top-Down Integration Tests using Stubs.

These tests test the Service module (high-level) with stubbed dependencies
(Storage and Notifier) to verify the integration logic before lower-level
modules are fully implemented.
"""
import pytest
from src.service import Service


class StorageStub:
    """Stub implementation of Storage for Top-Down testing."""
    
    def __init__(self, should_fail=False):
        self.tasks = []
        self.should_fail = should_fail
        self.save_called = False
        self.save_called_with = None
    
    def save(self, task):
        self.save_called = True
        self.save_called_with = task
        if self.should_fail:
            raise Exception("Storage failed")
        self.tasks.append(task)
        return True
    
    def get_all(self):
        return self.tasks.copy()


class NotifierStub:
    """Stub implementation of Notifier for Top-Down testing."""
    
    def __init__(self, should_fail=False):
        self.notifications = []
        self.should_fail = should_fail
        self.send_called = False
        self.send_called_with = None
    
    def send(self, message):
        self.send_called = True
        self.send_called_with = message
        if self.should_fail:
            raise Exception("Notifier failed")
        self.notifications.append(message)
        return True
    
    def get_notifications(self):
        return self.notifications.copy()


class TestTopDownIntegration:
    """Top-Down integration tests using stubs."""
    
    def test_service_with_stubs_basic_flow(self):
        """Test basic flow with stubbed dependencies."""
        storage_stub = StorageStub()
        notifier_stub = NotifierStub()
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        result = service.add_task("Test Task", "Test Description")
        
        # Verify return value
        assert result is True
        
        # Verify that service interacted with stubs
        assert storage_stub.save_called is True
        assert notifier_stub.send_called is True
        
        # Verify the arguments passed to stubs
        assert storage_stub.save_called_with['title'] == "Test Task"
        assert "Test Task" in notifier_stub.send_called_with
    
    def test_service_with_storage_failure(self):
        """Test behavior when storage fails."""
        storage_stub = StorageStub(should_fail=True)
        notifier_stub = NotifierStub()
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        # Should raise exception when storage fails
        with pytest.raises(Exception, match="Storage failed"):
            service.add_task("Test Task")
        
        # Notifier should not have been called
        assert notifier_stub.send_called is False
    
    def test_service_with_notifier_failure(self):
        """Test behavior when notifier fails."""
        storage_stub = StorageStub()
        notifier_stub = NotifierStub(should_fail=True)
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        # Should still succeed (notification failure is handled)
        result = service.add_task("Test Task")
        assert result is True
        
        # Storage should have been called
        assert storage_stub.save_called is True
        assert len(storage_stub.tasks) == 1
    
    def test_service_with_empty_title(self):
        """Test validation with empty title."""
        storage_stub = StorageStub()
        notifier_stub = NotifierStub()
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        # Should raise ValueError for empty title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("")
        
        # Neither storage nor notifier should have been called
        assert storage_stub.save_called is False
        assert notifier_stub.send_called is False
    
    def test_service_with_whitespace_title(self):
        """Test validation with whitespace-only title."""
        storage_stub = StorageStub()
        notifier_stub = NotifierStub()
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        # Should raise ValueError for whitespace-only title
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("   ")
        
        # Neither storage nor notifier should have been called
        assert storage_stub.save_called is False
        assert notifier_stub.send_called is False
    
    def test_service_integration_consistency(self):
        """Test that service maintains consistency across multiple operations."""
        storage_stub = StorageStub()
        notifier_stub = NotifierStub()
        service = Service(storage=storage_stub, notifier=notifier_stub)
        
        # Add multiple tasks
        service.add_task("Task 1")
        service.add_task("Task 2")
        service.add_task("Task 3")
        
        # Verify all were saved
        assert len(storage_stub.tasks) == 3
        assert len(notifier_stub.notifications) == 3
        
        # Verify order is preserved
        assert storage_stub.tasks[0]['title'] == "Task 1"
        assert storage_stub.tasks[1]['title'] == "Task 2"
        assert storage_stub.tasks[2]['title'] == "Task 3"
