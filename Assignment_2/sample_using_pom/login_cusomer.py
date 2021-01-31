import json
import time

from selenium.webdriver.common.by import By

dcloud_file = 'site.json'

# Read file
readfile = open(dcloud_file,"r")
data=json.load(readfile)
print(data)

# Open url
url=data['url']
email_id=data['email']
password=data['password']

print(url)
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver')
browser.get(url)
browser.implicitly_wait(10)

HOME_PAGE=(By.XPATH,'//small[.="http://www.phptravels.net"]')
MY_ACCOUNT = (By.XPATH, '//a[contains(.,"My Account")]')
LOG_IN = (By.XPATH, '//a[@href="https://www.phptravels.net/login"]')
EMAIL_ID = (By.XPATH, '//input[@name="username"]')
PASSWORD = (By.XPATH, '//input[@name="password"]')
SUBMIT = (By.XPATH, '//button[.="Login"]')
DEMO_ICON = (By.XPATH, '//a[contains(.,"Demo")]')
LOG_OUT = (By.XPATH, '//a[.="Logout"]')

browser.find_element(*HOME_PAGE).click()

title = browser.title
print(title)
assert title == 'Demo Script Test drive - PHPTRAVELS', 'Not expected title'
print(browser.window_handles)
time.sleep(5)
browser.switch_to.window(browser.window_handles[1])

title = browser.title
print(title)
assert title=='PHPTRAVELS | Travel Technology Partner', 'Not expected title'

browser.find_element(*MY_ACCOUNT).click()
browser.find_element(*LOG_IN).click()

time.sleep(5)
browser.find_element(*EMAIL_ID).send_keys(email_id)
browser.find_element(*PASSWORD).send_keys(password)
browser.find_element(*SUBMIT).click()

title = browser.title
print(title)
assert title=='Login', 'Not expected title'

browser.find_element(*DEMO_ICON).click()
browser.find_element(*LOG_OUT).click()






