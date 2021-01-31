import json

from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')

class Base:

    def __init__(self, browser):
        self.browser = browser

    def open(browser,url):
        browser.get(url)
        return browser

    def read_json(self,file_name):
        readfile = open(file_name, "r")
        data = json.load(readfile)
        print(data)
        return data
