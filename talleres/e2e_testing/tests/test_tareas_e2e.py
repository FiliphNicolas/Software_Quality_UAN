"""
Initial E2E tests - deliberately weak.

These tests are intentionally incomplete to demonstrate the need for
stronger E2E testing practices.
"""
import pytest


class TestTareasE2EInicial:
    """Initial E2E tests - deliberately weak."""
    
    def test_page_loads(self, page, app_server):
        """Test that the page loads successfully."""
        page.goto(app_server)
        
        # Very weak assertion - just checks that page loaded
        assert page.title() == "Gestor de Tareas"
    
    def test_create_task_clicks_button(self, page, app_server):
        """Test that clicking the create button doesn't crash."""
        page.goto(app_server)
        
        # Fill in the form
        page.fill('[data-testid="task-title-input"]', "Test Task")
        page.fill('[data-testid="task-description-input"]', "Test Description")
        
        # Click the button - but don't verify anything was actually created
        page.click('[data-testid="create-task-button"]')
        
        # Weak assertion - just checks we're still on the page
        assert page.url == app_server + "/"
    
    def test_complete_task_clicks_button(self, page, app_server):
        """Test that clicking complete button doesn't crash."""
        page.goto(app_server)
        
        # Create a task first
        page.fill('[data-testid="task-title-input"]', "Task to Complete")
        page.click('[data-testid="create-task-button"]')
        
        # Try to click complete - but don't verify it actually completed
        complete_button = page.locator('[data-testid="complete-button"]').first
        if complete_button.is_visible():
            complete_button.click()
        
        # Weak assertion - just checks we're still on the page
        assert page.url == app_server + "/"
    
    def test_delete_task_clicks_button(self, page, app_server):
        """Test that clicking delete button doesn't crash."""
        page.goto(app_server)
        
        # Create a task first
        page.fill('[data-testid="task-title-input"]', "Task to Delete")
        page.click('[data-testid="create-task-button"]')
        
        # Try to click delete - but don't verify it actually deleted
        delete_button = page.locator('[data-testid="delete-button"]').first
        if delete_button.is_visible():
            delete_button.click()
        
        # Weak assertion - just checks we're still on the page
        assert page.url == app_server + "/"
