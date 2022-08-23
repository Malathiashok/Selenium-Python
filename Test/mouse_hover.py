import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()
time.sleep(2)

admin = driver.find_element(By.XPATH, '//*[@id="menu_admin_viewAdminModule"]/b')
usr_mgt = driver.find_element(By.XPATH, "//*[@id='menu_admin_UserManagement']")
users = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewSystemUsers']")

# Move to mouse

act = ActionChains(driver)

act.move_to_element(admin).move_to_element(usr_mgt).move_to_element(users).click().perform()
# act.move_to_element('admin')
# act.move_to_element('usr_mgt')
# act.move_to_element('users')
# act.click()
# act.perform()
driver.quit()
