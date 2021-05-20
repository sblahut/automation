################################################################################################
################ World Courier Site Automation Events Filter Test Script #######################
################################################################################################


import time
from itertools import islice
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Declare Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

scriptStart = datetime.now()

def test_abcWorldCourierEventsFilter ():
    
    print('....Navigating to www.worldcourier.com/news-and-events/events....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Filter Functionality ######')

    # Open wc website
    driver.get('https://www.worldcourier.com/news-and-events/events')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()
    
    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############ Upcoming Events #############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Past Events
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.tab-nav > div.tab-nav__nav > div > div > nav > a:nth-child(2)").click()
    
    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Past Events ###############")
    for id in islice(ids, 0, 10, 1):
        print("Date: " + str(id.text))
        #count +=1
        #if id.count == 5:
        #        break
    print("##########################################")
    print("                                          ") 

   

# Call Method
test_abcWorldCourierEventsFilter ()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
################ World Courier Site Automation Events Filter Test Script #######################
################################################################################################