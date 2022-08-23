from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

email_box = driver.find_element(By.XPATH, "//input[@id='Email']")

email_box.clear()
email_box.send_keys("abc@gmail.com")  #inner text of the element print nothing

print("Text: ", email_box.text)
print("get attriput Text: ", email_box.get_attribute('value')) # print the value of the element

driver.quit()