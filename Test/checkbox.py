import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))

for checkbox in checkboxes:
    checkbox.click()

#select multiple checkboxes-----
#for checkbox in checkboxes:
#    weekname = checkbox.get_attribute('id')
 #   if weekname == 'monday' or weekname == 'sunday':
  #      checkbox.click()
""""""""


# ---select lastt two checkboxes---
#for i in range(len(checkboxes)-2, len(checkboxes)):
 #   checkboxes[i].click()



 #---select only first two---
#for i in range(len(checkboxes)):
#    if i < 2:
#        checkboxes[i].click()

#----unselect the checkboxes=---
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

driver.quit()
