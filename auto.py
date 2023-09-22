from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import smtpd

#This is simple safe automation built to exercise some of the 'bot' functionality that selenium has! I used this website in particular becasue its was safe to test a webscrapper on.
#PLEASE know that many websites dont like webscrappers and prohibit this type of activity so be aware of where you scrape.
#HAPPY SCRAPPING :)

options = webdriver.ChromeOptions() 
options.binary_location = "/usr/bin/google-chrome" #Need to point to location of chromedriver in WSL
driver = webdriver.Chrome(options=options)
# options.add_argument("--headless")  # Optional: Run Chrome in headless mode

driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(8)

lang_menu = driver.find_element(By.ID, "promptContentChangeLanguage")
lang_eng = lang_menu.find_element(By.ID, "langSelect-EN")
lang_eng.click()

driver.implicitly_wait(5)

for i in range(100):
    cookie = driver.find_element(By.ID, "bigCookie")
    cookie_count = driver.find_element(By.ID, "cookies")
    items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1) ]

    #Actions chains are like a queue of actions to perform
    actions = ActionChains(driver)
    actions.click(cookie)
    actions.perform() #Need perform to execute 

    count = int(cookie_count.text.split(" ")[0])
    
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    
    # Print the number of cookies and other relevant information
    # print(f"Cookies: {cookie_count.text}, Items: {[item.text for item in items]}")

time.sleep(5)
driver.quit()