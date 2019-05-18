import time

class LoginPage():

    def __init__(self, driver):

        self.driver = driver
        self.driver.email = "//input[@name='email_address']"
        self.driver.password = "//input[@name='password']"
        self.driver.signin = "//span[contains(text(),'Sign In')]"


    def email(self,email):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.driver.email).click()
        self.driver.find_element_by_xpath(self.driver.email).send_keys(email)
    def password(self,password):
        self.driver.find_element_by_xpath(self.driver.password).click()
        self.driver.find_element_by_xpath(self.driver.password).send_keys(password)
    def signin(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(self.driver.signin).click()