from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.monsterindia.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@class='uprcse semi-bold']").click()
driver.find_element(By.XPATH, '//*[@id="file-upload"]').send_keys("C:\Drivers\language-kannada.pdf")
