import pytest
import subprocess
import time
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))


@pytest.fixture(scope="session")
def app_server():
    """Start the Flask application server for E2E testing."""
    # Start the Flask server in a subprocess
    server_process = subprocess.Popen(
        [sys.executable, "src/app.py"],
        cwd=Path(__file__).parent.parent,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for the server to start
    time.sleep(3)
    
    yield "http://localhost:5000"
    
    # Cleanup: stop the server
    server_process.terminate()
    server_process.wait(timeout=5)


@pytest.fixture
def page(app_server):
    """Create a new Playwright page for each test."""
    from playwright.sync_api import sync_playwright
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        yield page
        
        context.close()
        browser.close()


@pytest.fixture(autouse=True)
def reset_tasks():
    """Reset tasks before each test to ensure isolation."""
    import os
    import json
    
    data_file = Path(__file__).parent.parent / 'data' / 'tasks.json'
    if data_file.exists():
        data_file.unlink()
    
    # Ensure data directory exists
    data_dir = Path(__file__).parent.parent / 'data'
    data_dir.mkdir(exist_ok=True)
    
    yield
