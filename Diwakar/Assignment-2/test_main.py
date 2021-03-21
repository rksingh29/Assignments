import pytest
from selenium import webdriver
from assignment.loginpage import LoginPage

@pytest.fixture
def setup():
    driver = webdriver.Chrome(executable_path='/home/diwakar/Desktop/chromedriver_linux64/chromedriver')
    driver.get("https://www.phptravels.net/login")
    driver.maximize_window()
    yield driver

    driver.quit()


def test_login(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.enter_email("user@phptravels.com")
    loginpage.enter_password("demouser")
    loginpage.click_login()
