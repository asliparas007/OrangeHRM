import time

from Utils.comman_function import login_as_user


def test_dashboard(initialize_broswer):
    driver = initialize_broswer
    login_as_user(driver)
    time.sleep(5)