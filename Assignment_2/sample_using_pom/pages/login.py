from selenium.webdriver.common.by import By


class Login:

    LOG_IN = (By.XPATH, '//a[@href="https://www.phptravels.net/login"]')
    EMAIL_ID = (By.XPATH, '//input[@name="username"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    SUBMIT = (By.XPATH, '//button[.="Login"]')

    def __init__(self, browser):
        self.browser = browser

    def login(self, email_id, password):
        self.browser.find_element(*self.EMAIL_ID).send_keys(email_id)
        self.browser.find_element(*self.PASSWORD).send_keys(password)
        self.browser.find_element(*self.SUBMIT).click()
        return self.browser


