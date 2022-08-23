from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe.exe")
driver = webdriver.Chrome(service = serv_obj)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions =[NoSuchElementException,
                                                      ElementNotVisibleException,
                                                      ElementNotVsibleException, Exception])

driver.get("https://google.com/")
driver.maximize_window()

search_box = driver.find_element(By.NAME,'q')

search_box.send_keys("Selenium")
search_box.submit()

searchlink = mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
searchlink.click()
#time.sleep(10)
driver.quit()