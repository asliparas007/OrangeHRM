from selenium.webdriver.common.by import By


class dashBoard():
    def __init__(self,driver):
        self.driver = driver
        self.get_recruitment = (By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"][5]')

    def click_recruitment_option(self):
        self.driver.find_element(*self.get_recruitment).click()