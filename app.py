from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions() 
options.binary_location = "/usr/bin/google-chrome" #Need to point to location of chromedriver in WSL
driver = webdriver.Chrome(options=options)

# Optional: Run Chrome in headless mode
# options.add_argument("--headless")

#Add a website that you wish to scrape
driver.get("https://toscrape.com.usitestat.com/")

# Uncomment code below to run a simple test for Selenium
####################### 
# title_element = driver.title
# print(driver.title)
#######################

search = driver.find_element("name", "q") #Finds the search bar by name
search.send_keys("test") #Tells Selenium to input "test" into the search bar
search.send_keys(Keys.RETURN) #Tells Selenium to hit 'ENTER'

#Sometimes the page loads slower than the pace Selenium is scrapping. This will result in a 'element not found' error most times. 
#We use WebDriverWait() to tell selenium to wait x amount of seconds until excepcted conditions are present.
#In addition we use a try & finally in order to control the execution of the code within the try block. If there is any errors it will default to the finally block which is to quit the browser. 
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

