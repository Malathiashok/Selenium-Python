import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#open the link
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()


#total no links

links = driver.find_elements(By.XPATH,'//a')
print("Total no of links:" ,len(links))

#print all the links:

for link in links:
    print(link.text)

driver.quit()