from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time


#############test


options = Options()
options.add_experimental_option("prefs", {
"download.default_directory": "C:\\Users\\tung.nguyen\\Desktop\\0 Project\\stock\\data\\vn_investing",
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True
})

driver = webdriver.Chrome("C:/Users/tung.nguyen/Desktop/0 Project/chromedriver_win32/chromedriver.exe", options = options)
driver.get("https://vn.investing.com/rates-bonds/vietnam-10-year-bond-yield-historical-data")

#wait & close banner
time.sleep(20)
#close banner
try:
    driver.find_elements(By.CLASS_NAME, 'popupCloseIcon.largeBannerCloser')[0].click()
    print("close banner")
except:
    print("banner already closed")

#login 
driver.find_elements(By.CLASS_NAME, 'login.bold')[0].click()
driver.find_elements(By.ID, 'loginFormUser_email')[0].send_keys("thanhtung211995@gmail.com")
driver.find_elements(By.ID, 'loginForm_password')[0].send_keys("BkkWwkaL123")
driver.find_elements(By.CLASS_NAME, 'newButton.orange')[2].click()


#select data & download

driver.execute_script("window.scrollTo(0, 699)") 
driver.find_elements(By.ID, 'datePickerIconWrap')[1].click()
driver.find_elements(By.ID, 'startDate')[0].clear()
driver.find_elements(By.ID, 'startDate')[0].send_keys("01/01/2000")
driver.find_elements(By.ID, 'endDate')[0].clear()
driver.find_elements(By.ID, 'endDate')[0].send_keys("01/01/2030")
driver.find_elements(By.ID, 'applyBtn')[0].click()
driver.find_elements(By.CLASS_NAME, 'newBtn.LightGray.downloadBlueIcon.js-download-data')[0].click()


