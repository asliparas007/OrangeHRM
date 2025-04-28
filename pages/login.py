from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.get_username = (By.XPATH, "//input[@name='username']")
        self.get_password = (By.XPATH,"//input[@name='password']")
        self.get_login_button = (By.XPATH, "//button[text()=' Login ']")

    def loginuser(self,username,password):
        self.driver.find_element(*self.get_username).send_keys(username)
        self.driver.find_element(*self.get_password).send_keys(password)
        self.driver.find_element(*self.get_login_button).click()
