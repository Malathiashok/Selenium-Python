from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)


driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,'//*[@id="inputText1"]').send_keys("Welcome to test")
input2 = driver.find_element(By.XPATH,'//*[@id="inputText2"]')

action = ActionChains(driver)

action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

action.send_keys(Keys.TAB).perform()

action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

driver.close()

