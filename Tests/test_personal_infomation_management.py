import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.personalInformationManagement import PersonalInformationManagement
from Utils.comman_function import login_as_user


def test_personal_information_management(initialize_broswer):
    driver = initialize_broswer
    login_as_user(driver)
    pim_page = PersonalInformationManagement(driver)
    pim_page.select_PIM()
    pim_page.add_employee("test123","test123")
    pim_page.check_toast()

