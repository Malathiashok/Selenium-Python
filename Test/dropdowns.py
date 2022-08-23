import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drp_dwn = driver.find_element(By.XPATH,"//select[@id='input-country']")
drp_country = Select(drp_dwn)
#drp_country = Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select from dropdown

#drp_country.select_by_visible_text("India")
#drp_country.select_by_value("17")
#drp_country.select_by_index(20)
#time.sleep(2)

#select all options count and print them

#all_options = drp_country.options
#print("Total optios: ", len(all_options))

#for opt in all_options:
#    print(opt.text)

#=== select optons without ussing built in operatios===
#for opt in all_options:
#    if opt.text == "india":
#        opt.click
#        break

# ----if tag name is not "Select"---
alloptions = drp_country.options
print("Total optios: ", len(alloptions))
driver.quit()