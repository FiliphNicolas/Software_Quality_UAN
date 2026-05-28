"""
Improved Integration Tests with Enhanced Coverage.

These tests extend the integration coverage to include:
- Failure during storage
- Failure during notification
- Empty titles
- Duplicate tasks
- System consistency during partial failures
"""
import pytest
from unittest.mock import Mock
from src.service import Service
from src.storage import Storage
from src.notifier import Notifier


class TestIntegrationImprovedCoverage:
    """Improved integration tests with enhanced coverage."""
    
    def test_storage_failure_prevents_notification(self):
        """
        Test that when storage fails, notification is not sent.
        This maintains system consistency by not notifying about unsaved tasks.
        """
        storage_mock = Mock()
        storage_mock.save.side_effect = Exception("Storage failed")
        notifier_mock = Mock()
        
        service = Service(storage=storage_mock, notifier=notifier_mock)
        
        # Should raise exception when storage fails
        with pytest.raises(Exception, match="Storage failed"):
            service.add_task("Test Task")
        
        # Verify storage was called
        storage_mock.save.assert_called_once()
        
        # Verify notification was NOT called (consistency maintained)
        notifier_mock.send.assert_not_called()
    
    def test_notification_failure_does_not_prevent_storage(self):
        """
        Test that when notification fails, the task is still saved.
        This maintains system consistency by ensuring data is preserved.
        """
        storage_mock = Mock()
        notifier_mock = Mock()
        notifier_mock.send.side_effect = Exception("Notification failed")
        
        service = Service(storage=storage_mock, notifier=notifier_mock)
        
        # Should still succeed (notification failure is handled gracefully)
        result = service.add_task("Test Task")
        assert result is True
        
        # Verify storage was called
        storage_mock.save.assert_called_once()
        
        # Verify notification was attempted
        notifier_mock.send.assert_called_once()
    
    def test_empty_title_raises_value_error(self):
        """Test that empty titles are rejected with ValueError."""
        service = Service()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("")
        
        # Verify nothing was saved
        assert len(service.get_tasks()) == 0
        assert len(service.get_notifications()) == 0
    
    def test_whitespace_only_title_raises_value_error(self):
        """Test that whitespace-only titles are rejected."""
        service = Service()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("   ")
        
        # Verify nothing was saved
        assert len(service.get_tasks()) == 0
        assert len(service.get_notifications()) == 0
    
    def test_none_title_raises_value_error(self):
        """Test that None titles are rejected."""
        service = Service()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task(None)
        
        # Verify nothing was saved
        assert len(service.get_tasks()) == 0
        assert len(service.get_notifications()) == 0
    
    def test_duplicate_task_raises_value_error(self):
        """Test that duplicate tasks are rejected."""
        service = Service()
        
        # Add first task
        service.add_task("Duplicate Task")
        
        # Try to add duplicate
        with pytest.raises(ValueError, match="already exists"):
            service.add_task("Duplicate Task")
        
        # Verify only one task was saved
        tasks = service.get_tasks()
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Duplicate Task"
        
        # Verify only one notification was sent
        notifications = service.get_notifications()
        assert len(notifications) == 1
    
    def test_case_sensitive_duplicate_detection(self):
        """Test that duplicate detection is case-sensitive."""
        service = Service()
        
        # Add task
        service.add_task("Task")
        
        # Add same task with different case (should be allowed)
        service.add_task("task")
        
        # Verify both tasks were saved
        tasks = service.get_tasks()
        assert len(tasks) == 2
    
    def test_system_consistency_with_partial_failure_notification(self):
        """
        Test system consistency when notification fails but storage succeeds.
        The task should be saved and the system should remain consistent.
        """
        storage = Storage()
        notifier_mock = Mock()
        notifier_mock.send.side_effect = Exception("Notification failed")
        
        service = Service(storage=storage, notifier=notifier_mock)
        
        # Add task with failing notification
        result = service.add_task("Consistency Test")
        assert result is True
        
        # Verify task was saved
        tasks = storage.get_all()
        assert len(tasks) == 1
        assert tasks[0]['title'] == "Consistency Test"
        
        # Verify notification was attempted
        notifier_mock.send.assert_called_once()
    
    def test_system_consistency_with_partial_failure_storage(self):
        """
        Test system consistency when storage fails.
        Notification should not be sent to maintain consistency.
        """
        storage_mock = Mock()
        storage_mock.save.side_effect = Exception("Storage failed")
        notifier = Notifier()
        
        service = Service(storage=storage_mock, notifier=notifier)
        
        # Try to add task with failing storage
        with pytest.raises(Exception, match="Storage failed"):
            service.add_task("Consistency Test")
        
        # Verify no notification was sent
        notifications = notifier.get_notifications()
        assert len(notifications) == 0
    
    def test_multiple_tasks_with_mixed_failures(self):
        """Test adding multiple tasks where some operations fail."""
        storage = Storage()
        notifier_mock = Mock()
        
        # First task: both succeed
        notifier_mock.send.return_value = True
        service = Service(storage=storage, notifier=notifier_mock)
        service.add_task("Task 1")
        
        # Second task: notification fails
        notifier_mock.send.side_effect = Exception("Notification failed")
        service.add_task("Task 2")
        
        # Third task: both succeed again
        notifier_mock.send.side_effect = None
        notifier_mock.send.return_value = True
        service.add_task("Task 3")
        
        # Verify all tasks were saved
        tasks = storage.get_all()
        assert len(tasks) == 3
        assert tasks[0]['title'] == "Task 1"
        assert tasks[1]['title'] == "Task 2"
        assert tasks[2]['title'] == "Task 3"
    
    def test_description_with_empty_title_still_validates(self):
        """Test that description doesn't bypass title validation."""
        service = Service()
        
        with pytest.raises(ValueError, match="Title cannot be empty"):
            service.add_task("", "Valid description")
        
        # Verify nothing was saved
        assert len(service.get_tasks()) == 0
    
    def test_long_title_is_handled(self):
        """Test that very long titles are handled correctly."""
        service = Service()
        
        long_title = "A" * 1000
        result = service.add_task(long_title)
        
        assert result is True
        tasks = service.get_tasks()
        assert len(tasks) == 1
        assert tasks[0]['title'] == long_title
    
    def test_special_characters_in_title(self):
        """Test that special characters in titles are handled."""
        service = Service()
        
        special_title = "Task with !@#$%^&*()_+ special chars"
        result = service.add_task(special_title)
        
        assert result is True
        tasks = service.get_tasks()
        assert len(tasks) == 1
        assert tasks[0]['title'] == special_title
    
    def test_unicode_characters_in_title(self):
        """Test that unicode characters in titles are handled."""
        service = Service()
        
        unicode_title = "Tarea con ñ and é and 中文"
        result = service.add_task(unicode_title)
        
        assert result is True
        tasks = service.get_tasks()
        assert len(tasks) == 1
        assert tasks[0]['title'] == unicode_title
    
    def test_notification_message_format(self):
        """Test that notification messages are formatted correctly."""
        service = Service()
        
        service.add_task("Test Task")
        
        notifications = service.get_notifications()
        assert len(notifications) == 1
        assert "New task added: Test Task" in notifications[0]
    
    def test_task_data_integrity(self):
        """Test that task data is stored correctly without modification."""
        service = Service()
        
        title = "  Test Title  "
        description = "  Test Description  "
        
        service.add_task(title, description)
        
        tasks = service.get_tasks()
        assert len(tasks) == 1
        # Verify whitespace is trimmed
        assert tasks[0]['title'] == "Test Title"
        assert tasks[0]['description'] == "Test Description"
    
    def test_concurrent_task_addition_simulation(self):
        """Test that the system handles rapid sequential task additions."""
        service = Service()
        
        # Add multiple tasks rapidly
        for i in range(10):
            service.add_task(f"Task {i}")
        
        # Verify all were saved
        tasks = service.get_tasks()
        assert len(tasks) == 10
        
        # Verify order is preserved
        for i in range(10):
            assert tasks[i]['title'] == f"Task {i}"
