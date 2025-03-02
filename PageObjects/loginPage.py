from selenium.webdriver.common.by import By


class loginPage():
    def __init__(self,driver):
        self.driver = driver
        self.get_username = (By.XPATH,'//input[@name="username"]')
        self.get_password = (By.XPATH, '//input[@name="password"]')
        self.get_submitButton = (By.CSS_SELECTOR, 'button[type="submit"]')
    def get_userlogin(self,username,password):
        self.driver.find_element(*self.get_username).send_keys(username)
        self.driver.find_element(*self.get_password).send_keys(password)
        self.driver.find_element(*self.get_submitButton).click()

