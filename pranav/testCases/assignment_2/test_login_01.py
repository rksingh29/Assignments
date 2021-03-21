import pytest
from selenium import webdriver
from testCases.conf_test import setup
from pageObjects.Login_objects import LoginPage
from Utils.readProperties import ReadConfig
from Utils.logger import LogGen

class Test_01:
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getuserName()
    password = ReadConfig.getPassword()
    logger =LogGen.loggen()

    def test_homepageTitle(self,setup):
        self.logger.info('********** Test_01_Home Page Test ********')
        self.logger.info("********** Verifying Homepage ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == ReadConfig.getloginTitle():
            self.driver.close()
            self.logger.info("********** Test_01_Home Page Test is Passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********** Test_01_Home Page Test is Failed ********")
            assert False

    def test_login(self,setup):
        self.logger.info("********** Test_02_Admin Login Test ********")
        self.logger.info("********** Verifying Admin Login Test ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == ReadConfig.getadminTitle():
            self.driver.close()
            self.logger.info("********** Test_02_Admin Login Test is Passed ********")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.quit()
            self.logger.info("********** Test_02_Admin Login Test is Failed ********")
            assert False


