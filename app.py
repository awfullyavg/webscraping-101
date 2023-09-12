from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions() 
options.binary_location = "/usr/bin/google-chrome" #Need to point to location of chromedriver in WSL
driver = webdriver.Chrome(options=options)
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode

driver.get("https://toscrape.com.usitestat.com/")
# title_element = driver.title
# print(driver.title)

search = driver.find_element("name", "q")
search.send_keys("test")
search.send_keys(Keys.RETURN)


try:
    listings = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "content_wrapper"))
    )

    listings_elements = WebDriverWait(listings, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "listings"))
    )
   
    for listings_element in listings_elements:
            print(listings_element.text)
finally:
    driver.quit()

# print(listings.text)
# print(driver.page_source)
time.sleep(5)

driver.quit()

