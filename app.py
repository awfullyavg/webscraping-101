from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode
options.binary_location = "/usr/bin/google-chrome"


driver = webdriver.Chrome(options=options)

driver.get("https://toscrape.com.usitestat.com/")
# title_element = driver.title
# print(driver.title)

search = driver.find_element("name", "q")
search.send_keys("test")
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)

driver.quit()

