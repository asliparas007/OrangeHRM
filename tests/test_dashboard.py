import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.DashboardPage import dashBoard


def test_dashboard(valid_user_session):
    driver = valid_user_session
    assert "dashboard" in driver.current_url, "no url"
    link = driver.current_url
    print(link)

    time.sleep(5)