from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time
import os

location = os.getcwd()

def Chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
    preferences = {"download.default_directory": location
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option('prefs', preferences)
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    return driver

driver = Chrome_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")

driver.maximize_window()


driver.find_element(By.XPATH,'//tbody/tr[1]/td[3]/a[1]').click()