import pytest
from selenium import webdriver
from testCases.conf_test import setup
from pageObjects.Login_objects import LoginPage
import requests
from Utils import Xutils

from Utils.readProperties import ReadConfig
from Utils.logger import LogGen

class Test3 :
    baseURL = ReadConfig.getURL()
    logger =LogGen.loggen()

    def test_login_datadriven(self,setup):
        self.logger.info("********** Test_03_Admin Login Data Driven Test ********")

        self.logger.info("********** Verifying Admin Login Test for  ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        path = "/Testdata/testdata.xlsx"
        rows = Xutils.getRowCount(path, "Sheet1")

        for r in range(2,rows+1):
            username=Xutils.ReadData(path, "Sheet1", r, 1)
            password = Xutils.ReadData(path, "Sheet1", r, 2)
            self.lp.setUsername(username)
            self.lp.setPassword(password)
            self.lp.clickLogin()
            act_title = self.driver.title
            if act_title == ReadConfig.getadminTitle():
                self.logger.info("********** Test_02_Admin Login Test is Passed ********")
                Xutils.writeData(path, "Sheet1", r, 3,"test Passed")
            else:
                self.logger.info("********** Test_02_Admin Login Test is Failed ********")
                Xutils.writeData(path, "Sheet1", r, 3, "test Failed")
