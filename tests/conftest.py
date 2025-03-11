import json
import os
import time

import pytest
from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service

from PageObjects.loginPage import loginPage

driver = None  # Global WebDriver instance
#New Content
def pytest_addoption(parser):
    print("pytest_addoption is running!")  # Debugging
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="function")
def initialize_browser(request):
    try:
        browser_name = request.config.getoption("browser_name", default="chrome")
    except ValueError:
        browser_name = "chrome" #fallback

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(4)
    driver.maximize_window()
    yield driver
    driver.quit()

#----------------------------------------------------
test_data_path = os.path.join(os.path.dirname(__file__), "../data/test_login.json") # -> check directory and file path and make union
test_data_path = os.path.abspath(test_data_path)  # -> Convert to absolute path
with open(test_data_path) as f:                   #-> open file as read mode
    test_data = json.load(f)                      #-> convert file into dict
    test_list = test_data["data"]                 #-> extract and load
@pytest.fixture()
def valid_user_session(initialize_browser):
    """Fixture to log in only the first valid user from test_login.json."""

    valid_user = None  # Initialize valid_user as None

    for item in test_list:  # Iterate over each item in test_list
        if item["expected"] == "dashboard":  # Check if the "expected" key has the value "dashboard"
            valid_user = item  # Assign the first matching item to valid_user
            break  # Stop searching once we find the first valid user

    if not valid_user:
        pytest.skip("No valid user found in test data")
    driver = initialize_browser
    userlogin = loginPage(driver)
    # (1) Track requests before login
    initial_requests = len(driver.requests)

    userlogin.get_userlogin(valid_user["username"], valid_user["password"])
    time.sleep(3)
    # Ensure login was successful
    if "/dashboard" not in driver.current_url:
        pytest.skip("Skipping test: Login failed")

    # Check API request
    target_api_endpoint = 'auth/validate'
    new_requests = driver.requests[initial_requests:]

    for request in new_requests:
        if request.response and target_api_endpoint in request.url:
            status_code = request.response.status_code
            print(f"API Request: {request.url} | Status Code: {status_code}")

            # Check if the response is 302
            if status_code == 302:
                print("✅ 'auth/validate' request returned 302 Found.")
            else:
                print(f"⚠️ 'auth/validate' request returned {status_code} instead of 302.")
            break  # Stop checking once we find the request

    return driver

#---------------------------------------- Report-----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Capture screenshot on test failure and embed in HTML report fle.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'Reports')
            os.makedirs(reports_dir, exist_ok=True)

            safe_test_name = report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")
            file_name = os.path.join(reports_dir, safe_test_name + ".png")

            print("Test failed! Capturing screenshot:", file_name)

            # Get the driver from the test's fixture
            driver = item.funcargs.get("initialize_browser")

            if driver is not None:  # Ensure driver is initialized
                _capture_screenshot(driver, file_name)  # Pass driver

                # Convert path for pytest-html
                rel_file_name = os.path.relpath(file_name, os.path.dirname(__file__))
                rel_file_name = rel_file_name.replace("\\", "/")  # Ensure correct format

                if os.path.exists(file_name):
                    html = f'<div><img src="{rel_file_name}" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>'
                    extra.append(pytest_html.extras.html(html))

        report.extra = extra

# `_capture_screenshot()` to accept `driver`
def _capture_screenshot(driver, file_name):
    if driver is not None:
        driver.get_screenshot_as_file(file_name)
    else:
        print("Error: WebDriver is not initialized!")


