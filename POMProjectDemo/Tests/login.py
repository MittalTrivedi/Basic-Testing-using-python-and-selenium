from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service("\\Users\\mittaltrivedi\\Documents\\Selenium_Python_Testing\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element("name","username").send_keys("Admin")

driver.find_element("name","password").send_keys("admin123")

driver.find_element(By.CLASS_NAME,"oxd-button").click()

driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()

driver.find_element(By.LINK_TEXT,"Logout").click()

time.sleep(20)
driver.close()
driver.quit()
print("Test Completed")