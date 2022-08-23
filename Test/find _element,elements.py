from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

#Locator matcing wih single element
#element = driver.find_element(By.XPATH, '//input[@id=\'small-searchterms\']')
#element.send_keys("Apple MacBook Pro")

#Locator matcing wih multiple element
#element = driver.find_element(By.XPATH, '//div[@class='footer-block information']')
#print(element.text)

#element not available

#element = driver.find_element(By.LINKTEXT, 'LOG')
#element.click()


#####find elements
#Locator matcing wih single element
#element = driver.find_element(By.XPATH, '//input[@id=\'small-searchterms\']')
print(len(element))
#element[0].send_keys("Apple MacBook Pro")

#Locator matcing wih multiple element
#element = driver.find_element(By.XPATH, '//div[@class='footer-block information']')
#print(len(element))
#print(element[0].text)

#for ele in element:
    print(ele.text)

#element not available

#element = driver.find_element(By.LINKTEXT, 'LOG')
#print("element returned: ", len(element))


