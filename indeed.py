from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"
driver = webdriver.Chrome(options=options)

driver.get("https://www.indeed.com/")
driver.implicitly_wait(10)

job_search_bar = driver.find_element(By.XPATH, "//*[@id='text-input-what']")
location_search_bar = driver.find_element(By.XPATH, "//*[@id='text-input-where']")
job_search_bar.send_keys("System Administrator")
job_search_bar.send_keys(Keys.RETURN)

try:
    WebDriverWait(driver, 20).until(
        EC.url_contains("System Administrator")
    )
    time.sleep(5)
    URL = driver.current_url
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup)
except:
    driver.quit()

time.sleep(5)
driver.quit()