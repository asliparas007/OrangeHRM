import time

from selenium.webdriver.common.by import By

from pages.dashboard_page import Dashboard
from pages.viewemployeelist import ViewEmployeeList


def test_pim_add_employee(valid_user):
    driver = valid_user
    dashboard = Dashboard(driver)
    dashboard.get_pim_left_menu()


    viewemp = ViewEmployeeList(driver)
    viewemp.click_add_employee_option()
    viewemp.fill_empl_details()



def test_add_report(valid_user):
    driver = valid_user
    dashboard = Dashboard(driver)
    dashboard.get_pim_left_menu()
    driver.find_element(By.XPATH,"//a[text()='Reports']").click()
    driver.find_element(By.XPATH,"//button[text()=' Add ']").click()
    driver.find_element(By.XPATH,"//input[@placeholder='Type here ...']").send_keys("Test Report")
    dropdowns = driver.find_elements(By.CLASS_NAME,"oxd-icon.bi-caret-down-fill.oxd-select-text--arrow")
    selection_cretria = dropdowns[0]
    selection_cretria.click()
    dropdown_options = driver.find_elements(By.CLASS_NAME, 'oxd-select-option')
    for item in dropdown_options:
        if item.text == "Pay Grade":
            item.click()
            break

    time.sleep(5)
