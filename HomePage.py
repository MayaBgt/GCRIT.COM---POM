class HomePage():

    def __init__(self, driver):

        self.driver = driver
        self.driver.logoff = "//span[contains(text(),'Log Off')]"


    def logoff(self):
        self.driver.find_element_by_xpath(self.driver.logoff).click()