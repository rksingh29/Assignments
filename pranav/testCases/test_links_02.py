import pytest
from selenium import webdriver
from testCases.conf_test import setup
from pageObjects.Login_objects import LoginPage
import requests

from Utils.readProperties import ReadConfig
from Utils.logger import LogGen

class Test_02:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getuserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    a=[]

    def test_links(self,setup):
     self.driver = setup
     self.driver.get(self.baseURL)
     a = self.driver.find_elements_by_tag_name("a")
     for a in a:
        r = requests.head(a.get_attribute('href'))
        print(a.get_attribute('href'), r.status_code)


