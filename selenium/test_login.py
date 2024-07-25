from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get(\"http://example.com/login\")
    username = driver.find_element_by_name(\"username\")
    password = driver.find_element_by_name(\"password\")
    login_button = driver.find_element_by_name(\"submit\")

    username.send_keys(\"testuser\")
    password.send_keys(\"testpass\")
    login_button.click()

    assert \"Dashboard\" in driver.title

    driver.quit()
