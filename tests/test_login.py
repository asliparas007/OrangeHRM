import time

import pytest

from pages.login import LoginPage


@pytest.mark.parametrize("username, password", [
    ("Admin", "admin123"),
    ("Admin", "wrongpass"),
    ("wronguser", "admin123"),
    ("", ""),
])

def test_login(initialize_browser,username,password):
    driver = initialize_browser
    user_login = LoginPage(driver)
    user_login.loginuser(username,password)
    time.sleep(5)