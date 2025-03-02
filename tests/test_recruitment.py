import time

from selenium.webdriver.common.by import By

from PageObjects.DashboardPage import dashBoard


def test_dashboard(valid_user_session):
    driver = valid_user_session
    assert "dashboard" in driver.current_url, "no url"
    link = driver.current_url
    print(link)
    dashboard_option = dashBoard(driver)
    dashboard_option.click_recruitment_option()
    time.sleep(5)