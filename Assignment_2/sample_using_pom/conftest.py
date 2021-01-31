import json

import pytest
from selenium import webdriver
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from pages.home import HomePage
from pages.login import Login

@pytest.fixture(scope="session")
def getBrowser():
    browser = webdriver.Chrome('../sample_code/chromedriver')
    return browser


@pytest.fixture(scope="session")
def getData():
    data_file = '../sample_code/site.json'
    readfile = open(data_file, "r")
    data = json.load(readfile)
    return data


@pytest.fixture(scope="function")
def login_page(getBrowser, getData):
    browser = getBrowser
    browser.get(getData['url'])
    browser.implicitly_wait(10)
    homepage = HomePage(browser)
    home_login= homepage.login()
    login = Login(home_login)
    login.login(getData['email'], getData['password'])
    return browser


@pytest.fixture(scope="function")
def logout():
    print('logout')
    return "logout"
