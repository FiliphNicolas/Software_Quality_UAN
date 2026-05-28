"""
Sandwich (Hybrid) Integration Tests.

These tests combine real components with stubbed components to validate
partial integrations. This approach balances the advantages of both
Top-Down and Bottom-Up testing.
"""
import pytest
from src.service import Service
from src.storage import Storage
from src.notifier import Notifier


class NotifierStub:
    """Stub implementation of Notifier for Sandwich testing."""
    
    def __init__(self, should_fail=False):
        self.notifications = []
        self.should_fail = should_fail
    
    def send(self, message):
        if self.should_fail:
            raise Exception("Notifier failed")
        self.notifications.append(message)
        return True
    
    def get_notifications(self):
        return self.notifications.copy()


class StorageStub:
    """Stub implementation of Storage for Sandwich testing."""
    
    def __init__(self, should_fail=False):
        self.tasks = []
        self.should_fail = should_fail
    
    def save(self, task):
        if self.should_fail:
            raise Exception("Storage failed")
        self.tasks.append(task)
        return True
    
    def get_all(self):
        return self.tasks.copy()


class TestSandwichIntegration:
    """Sandwich integration tests combining real and stubbed components."""
    
    def test_real_storage_stub_notifier(self):
        """Test with real Storage but stubbed Notifier."""
        real_storage = Storage()
        notifier_stub = NotifierStub()
        service = Service(storage=real_storage, notifier=notifier_stub)
        
        result = service.add_task("Sandwich Task 1", "Real storage, stub notifier")
        
        # Verify operation succeeded
        assert result is True
        
        # Verify real storage was used
        tasks = real_storage.get_all()
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Sandwich Task 1"
        
        # Verify stub notifier was used
        notifications = notifier_stub.get_notifications()
        assert len(notifications) == 1
        assert "Sandwich Task 1" in notifications[0]
    
    def test_stub_storage_real_notifier(self):
        """Test with stubbed Storage but real Notifier."""
        storage_stub = StorageStub()
        real_notifier = Notifier()
        service = Service(storage=storage_stub, notifier=real_notifier)
        
        result = service.add_task("Sandwich Task 2", "Stub storage, real notifier")
        
        # Verify operation succeeded
        assert result is True
        
        # Verify stub storage was used
        tasks = storage_stub.get_all()
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Sandwich Task 2"
        
        # Verify real notifier was used
        notifications = real_notifier.get_notifications()
        assert len(notifications) == 1
        assert "Sandwich Task 2" in notifications[0]
    
    def test_real_storage_failing_notifier_stub(self):
        """Test real storage with failing notifier stub."""
        real_storage = Storage()
        notifier_stub = NotifierStub(should_fail=True)
        service = Service(storage=real_storage, notifier=notifier_stub)
        
        # Should still succeed (notification failure is handled)
        result = service.add_task("Task with failing notifier")
        assert result is True
        
        # Task should still be saved in real storage
        tasks = real_storage.get_all()
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Task with failing notifier"
    
    def test_failing_storage_stub_real_notifier(self):
        """Test failing storage stub with real notifier."""
        storage_stub = StorageStub(should_fail=True)
        real_notifier = Notifier()
        service = Service(storage=storage_stub, notifier=real_notifier)
        
        # Should raise exception when storage fails
        with pytest.raises(Exception, match="Storage failed"):
            service.add_task("Task with failing storage")
        
        # Notifier should not have been called
        notifications = real_notifier.get_notifications()
        assert len(notifications) == 0
    
    def test_sandwich_validation_with_real_storage(self):
        """Test validation logic with real storage."""
        real_storage = Storage()
        notifier_stub = NotifierStub()
        service = Service(storage=real_storage, notifier=notifier_stub)
        
        # Test empty title validation
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("")
        
        # Verify nothing was saved
        assert len(real_storage.get_all()) == 0
        assert len(notifier_stub.get_notifications()) == 0
    
    def test_sandwich_validation_with_real_notifier(self):
        """Test validation logic with real notifier."""
        storage_stub = StorageStub()
        real_notifier = Notifier()
        service = Service(storage=storage_stub, notifier=real_notifier)
        
        # Test empty title validation
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("")
        
        # Verify nothing was saved or notified
        assert len(storage_stub.get_all()) == 0
        assert len(real_notifier.get_notifications()) == 0
    
    def test_sandwich_duplicate_detection_with_real_storage(self):
        """Test duplicate detection with real storage."""
        real_storage = Storage()
        notifier_stub = NotifierStub()
        service = Service(storage=real_storage, notifier=notifier_stub)
        
        # Add first task
        service.add_task("Duplicate Task")
        
        # Try to add duplicate
        with pytest.raises(ValueError, match="already exists"):
            service.add_task("Duplicate Task")
        
        # Verify only one task was saved
        tasks = real_storage.get_all()
        assert len(tasks) == 1
        
        # Verify only one notification was sent
        notifications = notifier_stub.get_notifications()
        assert len(notifications) == 1
    
    def test_sandwich_multiple_operations_with_real_components(self):
        """Test multiple operations mixing real and stubbed components."""
        real_storage = Storage()
        real_notifier = Notifier()
        
        # First operation: real storage, stub notifier
        notifier_stub = NotifierStub()
        service1 = Service(storage=real_storage, notifier=notifier_stub)
        service1.add_task("Task 1")
        
        # Second operation: stub storage, real notifier
        storage_stub = StorageStub()
        service2 = Service(storage=storage_stub, notifier=real_notifier)
        service2.add_task("Task 2")
        
        # Verify real storage has Task 1
        real_tasks = real_storage.get_all()
        assert len(real_tasks) == 1
        assert real_tasks[0]['title'] == "Task 1"
        
        # Verify real notifier has Task 2
        real_notifications = real_notifier.get_notifications()
        assert len(real_notifications) == 1
        assert "Task 2" in real_notifications[0]
        
        # Verify stubs have their respective data
        assert len(storage_stub.get_all()) == 1
        assert len(notifier_stub.get_notifications()) == 1
    
    def test_sandwich_error_propagation_with_real_components(self):
        """Test error propagation with mixed real and stubbed components."""
        real_storage = Storage()
        notifier_stub = NotifierStub(should_fail=True)
        service = Service(storage=real_storage, notifier=notifier_stub)
        
        # Add task with failing notifier
        result = service.add_task("Error Test")
        
        # Should succeed (notification failure is handled)
        assert result is True
        
        # But task should still be saved in real storage
        tasks = real_storage.get_all()
        assert len(tasks) == 1
