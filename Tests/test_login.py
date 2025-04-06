
from Pages.login import LoginPage


def test_valid_login(initialize_broswer):
    driver = initialize_broswer
    login_page = LoginPage(driver)
    login_page.login("Admin","admin123")
    assert "dashboard" in driver.current_url.lower()