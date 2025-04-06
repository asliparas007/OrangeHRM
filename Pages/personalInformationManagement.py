from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PersonalInformationManagement:
    def __init__(self,driver):
        self.driver = driver
        self.get_pim_option = (By.CSS_SELECTOR,".oxd-main-menu-item-wrapper:nth-of-type(2)")
        self.get_add_option = (By.XPATH,"//button[contains(.,'Add')]")
        self.get_employee_container = (By.CLASS_NAME,"orangehrm-card-container")
        self.get_firstname = (By.NAME,"firstName")
        self.get_lastname = (By.NAME, "lastName")
        self.get_save_button = (By.XPATH,"//button[contains(.,'Save')]")
        self.get_toast_message = (By.CSS_SELECTOR,".oxd-toast-content.oxd-toast-content--success")

    def select_PIM(self):
        self.driver.find_element(*self.get_pim_option).click()
    def add_employee(self,firstname,lastname):
        self.driver.find_element(*self.get_add_option).click()
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(self.get_employee_container))
        self.driver.find_element(*self.get_firstname).send_keys(firstname)
        self.driver.find_element(*self.get_lastname).send_keys(lastname)
        self.driver.find_element(*self.get_save_button).click()

    def check_toast(self):
        toast_message = self.driver.find_element(*self.get_toast_message)
        print(toast_message.text)
        assert "Success" in toast_message.text