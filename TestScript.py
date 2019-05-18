import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage



class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/User/Documents/CACC/Module 5 - Automation/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)


    def test_login(self):
        driver = self.driver
        driver.get("http://www.gcrit.com/build3/login.php")
        driver.implicitly_wait(5)

        loginpage = LoginPage(driver)
        loginpage.email("maya.bogatskaya@gmail.com")
        loginpage.password("MayaCACC123456!")
        loginpage.signin()

        homepage = HomePage(driver)
        homepage.logoff()


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()




if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/User/PycharmProjects/Sel_Practice/venv/Lib/site-packages/HtmlTestRunner"),verbosity=2)
