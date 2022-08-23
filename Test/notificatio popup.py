import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ops = webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj, options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

