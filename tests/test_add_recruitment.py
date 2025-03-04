import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.AddRecruitmentPage import AddRecruitment


@pytest.mark.run(order=2)
def test_recruitment(valid_user_session):
    driver = valid_user_session
    # driver.get_screenshot_as_file("screenshot.png")
    recruitment_option = AddRecruitment(driver)
    recruitment_option.click_recruitment_option()
    recruitment_option.click_add_button()
    recruitment_option.add_candidate(firstname="john",lastname="John",email="abc@abc.com")
    #-------load and select from custom drop down
    recruitment_option.add_vacancy()
    #------------------------
    

