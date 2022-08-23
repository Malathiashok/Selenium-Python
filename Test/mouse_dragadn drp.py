import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
act = ActionChains(driver)

min_sli = driver.find_element(By.XPATH, "//body//div//span[1]")
max_sli = driver.find_element(By.XPATH, "//body//div//span[2]")

print("Location of sliders")
print(min_sli.location)
print(max_sli.location)


act.drag_and_drop_by_offset(min_sli, 100, 0).perform()

act.drag_and_drop_by_offset(min_sli, -39, 0).perform()
print("Location of sliders")
print(min_sli.location)
print(max_sli.location)

driver.quit()
