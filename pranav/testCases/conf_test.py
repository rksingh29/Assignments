from selenium import webdriver
from Utils.readProperties import ReadConfig
import pytest
import pytest_html
from py.xml import html
import pytest_metadata


@pytest.fixture()
def setup():
    driver = webdriver.Chrome(ReadConfig.getDriver())
    return driver


################################ pytest HTML report  ###############################

# for adding environment info into HTML Report
def pytest_configure(pytestconfig):
    pytestconfig._metadata["Project Name"] = 'nop Commerce'
    pytestconfig._metadata["Module Name"] = 'Admin login'
    pytestconfig._metadata["Tested by"] = 'Pranav Bartakke'

# hook to delete/modify Environment info to HTML report
#@pytest.mark.optionalhook

def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('Plugins', None)