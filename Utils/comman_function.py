from Pages.login import LoginPage


def login_as_user(driver):
    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")