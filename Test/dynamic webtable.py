import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# driver.find_element(By.ID, "txtUsername").send_keys("Admin")
# driver.find_element(By.ID, "txtPassword").send_keys("admin123")
# driver.find_element(By.ID, "btnLogin").click()
# time.sleep(5)

driver.find_element(By.XPATH, '//*[@id=\"menu_admin_viewAdminModule\"]').click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']").click()
driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']").click()
