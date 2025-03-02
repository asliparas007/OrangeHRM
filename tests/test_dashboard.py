

def test_dashboard(valid_user_session):
    driver = valid_user_session
    assert "dashboard" in driver.current_url, "no url"
    link = driver.current_url
    print(link)
    driver