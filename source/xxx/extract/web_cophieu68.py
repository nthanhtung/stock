from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

# cwd = os.getcwd()
# download_path = cwd + '\\data\\cophieu68'
# driver_path = "C:/Users/tung.nguyen/Desktop/0 Project/chromedriver_win32/chromedriver.exe"
# login_url ="https://www.cophieu68.vn/account/login.php"
# stock_url = "https://www.cophieu68.vn/export/excelfull.php?id=^vnindex"
# un = "thanhtung211995@gmail.com"
# pw = "BkkWwkaL123"

def get_cophieu68(driver_path, download_path, login_url, stock_url, un, pw):
    options = Options()
    options.add_experimental_option("prefs", {
    "download.default_directory": download_path,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(driver_path, options = options)
    driver.get(login_url)

    # login
    driver.find_elements(By.NAME, 'username')[1].send_keys(un)
    driver.find_elements(By.NAME, 'tpassword')[1].send_keys(pw)
    driver.find_elements(By.NAME, 'login')[0].click()

    # download data vn index
    driver.get(stock_url)
    return True


