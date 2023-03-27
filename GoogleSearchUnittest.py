from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class GoogleSearch(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        #driver = webdriver.Chrome()
        cls.s = Service("\\Users\\mittaltrivedi\\Documents\\Selenium_Python_Testing\\drivers\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.s)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
            
    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name","q").send_keys("Automation step by step")
        self.driver.find_element("name","btnK").click()
            
    def test_search_conestoga(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name","q").send_keys("Conestoga College")
        self.driver.find_element("name","btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



