from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

#driver = webdriver.Chrome()
s = Service("\\Users\\mittaltrivedi\\Documents\\Selenium_Python_Testing\\drivers\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome()

driver.set_page_load_timeout(10)
driver.get("https://google.com/search?q=Automation+step+by+step")

driver.maximize_window()
driver.refresh()

print ("Test completed successfully")