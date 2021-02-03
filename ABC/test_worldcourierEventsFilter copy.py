################################################################################################
################ World Courier Site Automation Events Filter Test Script #######################
################################################################################################

import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

# Set options variable
options = webdriver.ChromeOptions() 

count = 0

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.now()

def test_worldcourierEventsFilter():
    
    print('....Navigating to www.worldcourier.com/news-and-events/events....')

    # Open ash website
    driver.get('https://www.worldcourier.com/news-and-events/events')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()
    
    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############ Upcoming Events #############")
    for id in ids:
        
        print("Class: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Past Events
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.tab-nav > div.tab-nav__nav > div > div > nav > a:nth-child(2)").click()
    
    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Past Events ###############")
    for id in ids:
        count = 0       
        print("Class: " + str(id.text))
        count +=1
        if count == 5:
                break
    print("##########################################")
    print("                                          ") 

   

# Call Method
test_worldcourierEventsFilter()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
################ World Courier Site Automation Events Filter Test Script #######################
################################################################################################