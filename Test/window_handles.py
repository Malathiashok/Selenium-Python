import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

#window_id = driver.current_window_handle
#print(window_id)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
window_ids = driver.window_handles


##approach 1
# parent_window = window_ids[0]
# child_window = window_ids[1]
# print(parent_window, child_window)
# driver.switch_to.window(child_window)
# print("Title of child window", driver.title)
#
# driver.switch_to.window(parent_window)
# print("Title of parent window", driver.title)


#Approach 2
# for winid in window_ids:
#     driver.switch_to.window(winid)
#     print(winid.title())


#only some window closing
for winid in window_ids:
    driver.switch_to.window(winid)
    if driver.title == 'OrangeHRM'
        driver.close()




driver.quit()
