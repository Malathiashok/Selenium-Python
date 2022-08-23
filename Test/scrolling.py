
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#1.scroll down page

driver.execute_script("window.scrollBy(0,3000)","")
value = driver.execute_script("return window.pageYOffset;")

print("Number of pixels moved: ", value)

#2. scroll till teh page element
flag = driver.find_element(By.XPATH, "//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)

#3. scroll up and down till up and down
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)

driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved: ", value)

driver.quit()