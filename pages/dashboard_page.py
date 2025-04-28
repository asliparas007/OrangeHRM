import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Dashboard:
    def __init__(self,driver):
        self.driver = driver
        self.get_all_option = (By.CLASS_NAME, 'oxd-text.oxd-text--span.oxd-main-menu-item--name')

    def get_pim_left_menu(self):
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located(self.get_all_option))
        left_menu = self.driver.find_elements(*self.get_all_option)
        for menu_option in left_menu:
            if "PIM" == menu_option.text:
                menu_option.click()
                break

    time.sleep(5)
