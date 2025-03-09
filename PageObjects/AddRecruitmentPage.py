import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AddRecruitment():
    def __init__(self,driver):
        self.driver = driver
        self.get_recruitment = (By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"][5]')
        self.get_addbutton = (By.XPATH,"(//button[@type='button'])[5]")
        self.get_firstname = (By.NAME, "firstName")
        self.get_lastname = (By.NAME, "lastName")
        self.get_vacancy_section = (By.XPATH, "//div[@class='oxd-select-wrapper']")
        self.get_wait_element = (By.XPATH, "//div[contains(@class, 'oxd-select-dropdown')]")
        self.select_vacancy = (By.XPATH,"//div[@role='option'][5]")
        self.get_email = (By.XPATH, "//input[@placeholder='Type here']")
        self.get_submit_button = (By.XPATH,"//button[@type='submit']")

    def click_recruitment_option(self):
        self.driver.find_element(*self.get_recruitment).click()

    def click_add_button(self):
        self.driver.find_element(*self.get_addbutton).click()

    def add_candidate(self,firstname,lastname,email):
        self.driver.find_element(*self.get_firstname).send_keys(firstname)
        self.driver.find_element(*self.get_lastname).send_keys(lastname)
        self.driver.find_element(*self.get_email).send_keys(email)

    def add_vacancy(self):
        dropdown = self.driver.find_element(*self.get_vacancy_section)
        dropdown.click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((self.get_wait_element)))
        time.sleep(1)
        self.driver.find_element(*self.select_vacancy).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(*self.get_submit_button).click()
        toast_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//p[contains(@class,"oxd-toast-content-text")]')))
        assert "Success" in toast_message.text
        


