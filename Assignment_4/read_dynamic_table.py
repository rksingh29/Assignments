
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

url= 'https://in.finance.yahoo.com/quote/%5ENSEI?p=%5ENSEI'
HIST_DATA= (By.XPATH, '//span[.="Historical data"]')
TABLE = (By.XPATH, '//table')
HEADERS = (By.XPATH, '//thead/tr/th')
DATA_ROWS = (By.XPATH, '//tbody/tr')
DATA_TD = (By.XPATH, '//td')


browser = webdriver.Chrome('../Assignment_2/sample_code/chromedriver')
browser.get(url)
browser.maximize_window()
browser.implicitly_wait(10)
time.sleep(5)
browser.find_element(*HIST_DATA).click()
time.sleep(5)

table=browser.find_element(*TABLE)
headers = table.find_elements(*HEADERS)
theads=[]
for element in headers:
    theads.append(element.text)

rows={}
rowid=0
for elements in table.find_elements(*DATA_ROWS):
    temp=[]
    for element in elements.find_elements(*DATA_TD):
        theads.append(element.text)
    rows[rowid]=temp

print(rows)
print(theads)

browser.quit()




