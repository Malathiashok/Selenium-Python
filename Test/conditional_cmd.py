###-is_enabled(), is_disaplayed(), is_selected()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, '//input[@id=\'small-searchterms\']')

print("Satus: ", search_box.is_displayed())
print("Satus: ", search_box.is_enabled())
print("Satus: ", search_box.is_selected())

driver.close()


