import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.DashboardPage import dashBoard


@pytest.mark.run(order=2)
def test_recruitment(valid_user_session):
    driver = valid_user_session
    # driver.get_screenshot_as_file("screenshot.png")
    dashboard_option = dashBoard(driver)
    dashboard_option.click_recruitment_option()
    driver.find_element(By.XPATH,"(//button[@type='button'])[5]").click()
    driver.find_element(By.NAME, "firstName").send_keys("John")
    driver.find_element(By.NAME, "lastName").send_keys("John")
    #-------load and select from custom drop down
    dropdown = driver.find_element(By.XPATH, "//div[@class='oxd-select-wrapper']")
    dropdown.click()

    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class, 'oxd-select-dropdown')]")))
    #time.sleep(1)
    driver.find_element(By.XPATH,"//div[@role='option'][6]").click() #instead of loop directly access
    driver.find_element(By.XPATH, "//input[@placeholder='Type here']").send_keys("abc@abc.com")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    toast_message = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//p[contains(@class,"oxd-toast-content-text")]')))
    assert "Success" in toast_message.text

