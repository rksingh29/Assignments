
from    selenium import  webdriver

driver = webdriver.Chrome
string = 'admin'
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode(encoding='UTF-16',errors='strict')

# print result
print('The encoded version is:', string_utf)