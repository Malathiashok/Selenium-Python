from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("T-shirts")
driver.find_element(By.XPATH,"//button[@name='submit_search']").click()


#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


driver.close()
