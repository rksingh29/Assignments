from selenium import webdriver


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"
    link_logout_linktext = "Logout"


    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        ele = self.driver.find_element_by_id(self.textbox_username_id)
        ele.clear()
        ele.send_keys(username)


    def setPassword(self,password):
        ele1 = self.driver.find_element_by_id(self.textbox_password_id)
        ele1.clear()
        ele1.send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_Login_xpath).click()

    def ClickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

