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



    time.sleep(5)