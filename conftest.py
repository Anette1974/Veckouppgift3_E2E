# conftest.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1500)  # slow_mo = 300ms för att se bättre
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
