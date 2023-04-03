from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.s = Service("\\Users\\mittaltrivedi\\Documents\\Selenium_Python_Testing\\drivers\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.driver.find_element("name","username").send_keys("Admin")

        self.driver.find_element("name","password").send_keys("admin123")

        self.driver.find_element(By.CLASS_NAME,"oxd-button").click()

        self.driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()

        self.driver.find_element(By.LINK_TEXT,"Logout").click()

        time.sleep(20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
        
if __name__ == '__main__':
    unittest.main()

