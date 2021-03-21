class DymanictablePage:

    def __init__(self, driver):
        self.driver = driver
        self.table_xpath = "//table[@class='dataTable']"

    @property
    def table(self):
        return self.driver.find_element_by_xpath(self.table_xpath)
