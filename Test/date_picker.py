import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="dob"]').click()

datepic_month = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
datepic_month.select_by_visible_text("Dec")
datepic_year = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
datepic_year.select_by_visible_text("1990")

dates = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for date in dates.text:
    if date == '11':
        date.click()
        break