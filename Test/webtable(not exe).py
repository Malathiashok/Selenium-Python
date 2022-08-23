import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1. count number of rows and columns
noofrows = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
noofcols = driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th")

print(noofrows)
print(noofcols)

#2. read specific row and column
data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text # //*[@id="HTML1"]/div[1]/table/tbody/tr[5]/td[1]
#print(data)

#3.read all the cols and rows
# for r in range(2, noofrows+1):
#     for c in range(1, noofcols+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data)

#4.hoose only the author
for r in range(2, noofrows+1):
    authorname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(2)+"]").text
    if authorname == "Mukesh":
        bookname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]")
        print(bookname, authorname)