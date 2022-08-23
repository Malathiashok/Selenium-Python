#Authentication popups:
#syntax:
#http://username:pwd@test.com
#ex: https://admin:admin@the-internet.herokuapp.com/basic-auth/

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://admin:admin@the-internet.herokuapp.com/user_auth")
driver.maximize_window()
