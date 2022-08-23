from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)
driver.implicitly_wait(10)

driver.get("https://google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME,'q')

search_box.send_keys("Selenium")
search_box.submit()

#time.sleep(10)

driver.quit()