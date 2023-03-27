from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome()
s = Service("\\Users\\mittaltrivedi\\Documents\\Selenium_Python_Testing\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://google.com")

driver.find_element("name","q").send_keys("Automation step by step")

driver.find_element("name","btnK").click()

driver.close()

driver.quit()
print("Test Completed")