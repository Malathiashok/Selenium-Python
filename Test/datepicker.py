import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
#driver.find_element(By.XPATH,'//*[@id="datepicker"]').send_keys("05/15/2022")

year = "2020"
month = "March"
date = "13"

driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

while True:
    mon = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text   ###//*[@id="ui-datepicker-div"]/div/div/span[1]
    yr = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text
    if mon == month and yr ==year:
        break
    else:
        #driver.find_element(By.XPATH, "//a[@title='Next']").click()
        driver.find_element(By.XPATH,"//a[@title='Prev']").click()   ##//*[@id="ui-datepicker-div"]/div/a[1]
#select date


dates = driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")


for n in dates.text:
    if n == date:
        n.click()
        break


driver.quit()

