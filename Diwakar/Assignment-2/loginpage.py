class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_xpath = "//*[@name='username']"
        self.password_textbox_xpath = "//*[@name='password']"
        self.submit_button_xpath = "(//*[@type='submit'])[1]"

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()



