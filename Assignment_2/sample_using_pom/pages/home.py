import time

from selenium.webdriver.common.by import By


class HomePage:

    HOME_PAGE = (By.XPATH, '//small[.="http://www.phptravels.net"]')
    MY_ACCOUNT = (By.XPATH, '//a[contains(.,"My Account")]')
    LOG_IN = (By.XPATH, '//a[@href="https://www.phptravels.net/login"]')

    def __init__(self, browser):
        self.browser = browser

    def login(self):
        self.browser.find_element(*self.HOME_PAGE).click()

        title = self.browser.title
        print(title)
        assert title == 'Demo Script Test drive - PHPTRAVELS', 'Not expected title'
        print(self.browser.window_handles)
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[1])

        title = self.browser.title
        print(title)
        assert title == 'PHPTRAVELS | Travel Technology Partner', 'Not expected title'

        self.browser.find_element(*self.MY_ACCOUNT).click()
        self.browser.find_element(*self.LOG_IN).click()

        return self.browser








