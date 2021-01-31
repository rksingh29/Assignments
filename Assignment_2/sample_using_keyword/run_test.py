import json

from selenium import webdriver
from selenium.webdriver.common.by import By

import xpath_name



class Base:

    def __init__(self, browser):
        self.browser = browser

    def open(self,url):
        browser.get(url)
        return browser

    def read_json(self, file_name):
        readfile = open(file_name, "r")
        data = json.load(readfile)
        print(data)
        return data

    def click(self,path):
        print(type(path))
        browser.find_element(By.XPATH ,path).click()
        return browser


    def run_test_case(self,test_data):
        for step in test_data.keys():
            if test_data[step][0] == "login_to_url":
                url = test_data[step][1]
                self.open(url)
                browser.implicitly_wait(10)
            elif test_data[step][0] == "click_on_link":
                path = test_data[step][1]
                self.click(xpath_name.HOME_PAGE)



browser = webdriver.Chrome('../sample_code/chromedriver')

basecls = Base(browser)

suits = basecls.read_json('suits.json')

for suit in suits:
    print(suits[suit])
    testcases = suits[suit]
    for test_case in testcases:
        name = '{}.json'.format(test_case)
        test_data = basecls.read_json(name)
        print(test_data)
        basecls.run_test_case(test_data)
