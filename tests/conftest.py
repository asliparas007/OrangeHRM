import pytest
from selenium import webdriver

from pages.login import LoginPage


@pytest.fixture(scope="function")
def initialize_browser():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def valid_user(initialize_browser):
    driver = initialize_browser
    user_login = LoginPage(driver)
    user_login.loginuser("Admin", "admin123")
    yield driver
