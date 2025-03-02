import json
import os
import time


import pytest

from PageObjects.loginPage import loginPage
from tests.conftest import initialize_browser


test_data_path = os.path.join(os.path.dirname(__file__), "../data/test_login.json") # -> check directory and file path and make union
test_data_path = os.path.abspath(test_data_path)  # -> Convert to absolute path
with open(test_data_path) as f:                   #-> open file as read mode
    test_data = json.load(f)                      #-> convert file into dict
    test_list = test_data["data"]                 #-> extract and load
    #print("Loaded test data:", test_list)  ->  Debugging step


@pytest.mark.parametrize("test_item_list",test_list)
def test_userlogin(initialize_browser, test_item_list):
    # print(f"Running test with: {test_item_list}")
    # print(f"Type of test_item_list: {type(test_item_list)}")
    driver = initialize_browser
    userlogin = loginPage(driver)
    userlogin.get_userlogin(test_item_list["username"],test_item_list["password"])
    if test_item_list["expected"] == "dashboard":
        assert "/dashboard" in driver.current_url, f"Login failed for valid credentials: {test_item_list}"
    else:
        assert "/dashboard" not in driver.current_url, "Invalid login not redirected"

    time.sleep(5)


