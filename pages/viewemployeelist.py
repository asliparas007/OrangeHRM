from selenium.webdriver.common.by import By


class ViewEmployeeList:
    def __init__(self,driver):
        self.driver = driver
        self.get_add_employee_option = (By.LINK_TEXT, "Add Employee")
        self.get_first_name = (By.NAME, 'firstName')
        self.get_lastname = (By.NAME,'lastName')
        self.get_save_button = (By.XPATH, "//button[text()=' Save ']")

    def click_add_employee_option(self):
        self.driver.find_element(*self.get_add_employee_option).click()

    def fill_empl_details(self):
        self.driver.find_element(*self.get_first_name).send_keys("hello")
        self.driver.find_element(*self.get_lastname).send_keys("yellow")
        self.driver.find_element(*self.get_save_button).click()
