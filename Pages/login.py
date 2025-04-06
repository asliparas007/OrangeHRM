from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_username = (By.NAME,"username")
        self.get_password = (By.NAME,"password")
        self.get_login_button = (By.XPATH,"//button[@type='submit']")

    def login(self,username,password):
        self.driver.find_element(*self.get_username).send_keys(username)
        self.driver.find_element(*self.get_password).send_keys(password)
        self.driver.find_element(*self.get_login_button).click()