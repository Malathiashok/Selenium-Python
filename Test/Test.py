"""
1.Open browser
2. open url
3. enter username and password
4.click login
5.capture and verify the title of page
close the browser

"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")

driver = webdriver.Chrome(service = serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()

act_title = driver.title
exp_title = "OrangeHRM"
if act_title == exp_title:
    print("Test passed")
else:
    print("Test failed")
driver.close()




