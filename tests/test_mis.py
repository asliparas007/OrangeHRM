import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.conftest import valid_user_session


def test_Mis(valid_user_session):
    driver = valid_user_session
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    driver.find_element(By.XPATH, "(//div[@class='oxd-table-cell-actions'])[1]/button[2]").click()
    WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,'//div[@role="document"]')))
    driver.find_element(By.XPATH,"//button[contains(@class,'oxd-button--label-danger orangehrm-button-margin')]").click()
    time.sleep(5)
