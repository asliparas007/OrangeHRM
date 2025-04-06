import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def initialize_broswer():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
