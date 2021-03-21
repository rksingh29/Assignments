from datetime import time
from selenium import webdriver

driver = webdriver.Chrome()


def login(url, username, password):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
    driver.find_element_by_id('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_id('//*[@id="u_0_b"]').click()


def logout():
    logout = driver.find_element_by_id("userNavigationLabel")
    logout.click()
    time.sleep(20)
    logout1 = driver.find_element_by_partial_link_text('Log Out')
    logout1.click()
