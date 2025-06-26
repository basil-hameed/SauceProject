"""
Use conftest.py to manage the webdriver setup and teardown
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Previous driver setup
# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     driver.maximize_window()
#     yield driver
#     driver.quit()

# updated driver with cross browser testing
def get_driver(browser):
    if browser.lower() == "chrome":
        chrome_service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=chrome_service)
    elif browser.lower() == "firefox":
        firefox_service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=firefox_service)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.maximize_window()
    return driver

@pytest.fixture(scope="function")
def driver(request):
    browser = request.param  # Passed via test param
    driver = get_driver(browser)
    yield driver
    driver.quit()
