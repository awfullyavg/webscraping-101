from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import smtpd

options = webdriver.ChromeOptions() 
options.binary_location = "/usr/bin/google-chrome" #Need to point to location of chromedriver in WSL
driver = webdriver.Chrome(options=options)
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode

driver.get("https://toscrape.com.usitestat.com/")

# Uncomment code below to run a simple test for Selenium
####################### 
# title_element = driver.title
# print(driver.title)
#######################

search = driver.find_element("name", "q") #Finds the searchbar by name
search.send_keys("test") #Tells Selenium to input "test"
search.send_keys(Keys.RETURN) #Tells Selenium to hit 'ENTER'


#Sometimes the page loads slower than the pace Selenium is scrapping. This will result in a 'element not found' error most times. 
#We use WebDriverWait() to tell selenium to wait x amount of seconds until excepcted conditions are present.
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

#Code below demos simple navigation by finding a hyperlink named "Quia" & clicking it
# try:
#     link = WebDriverWait(driver, 10).until(
#          EC.presence_of_element_located((By.LINK_TEXT, "Quia"))
#     )
#     link.click()
#     print(driver.page_source)
    
# except:
#      driver.quit()


# print(listings.text)
# print(driver.page_source)

time.sleep(5)
driver.quit()

