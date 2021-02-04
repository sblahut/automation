################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
################################################################################################

import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from itertools import islice

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

testResult = ''

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.now()

def test_abcInnomarClinicLocator ():

    print('....Navigating to www.worldcourier.com/news-and-events/media-mentions....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Search Functionality ######')
    # Open innomar website
    driver.get('https://www.innomar-strategies.com/clinic-and-pharmacy-finder')

    # Search 'Seattle'
    search = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.location-finder > div.location-finder-search-wrapper.background-true-blue > div > div > div > form > div > label > input")
    
    search.send_keys("Seattle")

    search.click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "location-card__address")
    
    print("                                          ")
    print("##########################################")
    print("########## First Result: Seattle #########")
    for id in islice(ids, 0, 3, 1):
        
        print("Adress: " + str(id.text))
    print("##########################################")
    print("                                          ")

    


# Call Method
test_abcInnomarClinicLocator ()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  
















################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
################################################################################################