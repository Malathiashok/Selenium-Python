import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

time.sleep(3)

alert_window = driver.switch_to.alert
print(alert_window.text)
alert_window.send_keys("Welcome")
#alert_window.accept()

#####close the alert by cancel
alert_window.dismiss()




