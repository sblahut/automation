################################################################################################
##################### Xcenda Site Automation Decision Map Test Script ##########################
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
from selenium.common.exceptions import NoSuchElementException
# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.now()

def test_abcXcendaDecisionMap ():

    print('....Navigating to www.securos.com/catalog-selector....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Filter Functionality ######')
    # Open xcenda website
    driver.get('https://www.securos.com/catalog-selector')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

    # Select United States catalog
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div.marginator.margin-top-4.marginator-background-bright-white > div > div > div.card-row-cards.cards-hairline.background-light-gray > div > div > div:nth-child(1) > div > div > div > div.module__links > div > a > span").click()

    print('....Searching for saw....')

    try:
    # Search 'saw'
        search = driver.find_element(By.CSS_SELECTOR, "#ProductSearchBar > label > input")
        if search.is_displayed():
            search.send_keys('saw')
            driver.find_element(By.CSS_SELECTOR, "#ProductSearchButton").click()
    
    except NoSuchElementException:
        # Click instruments
        print('....Pulling category US Product Catalog / Instruments / Hand Instruments / Blade Handles / Microsurgical (Beaver®) Blade Handles....')
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div.module.module__card-row > div > div > div > div > div > div:nth-child(1) > div > div > div > a > div > span").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div > div > div:nth-child(1) > div > div > div > a > div > span").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div > div > div:nth-child(1) > div > div > div > a > div > span").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div > div > div:nth-child(1) > div > div > div > a > div > span").click()
    
    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "product-card__fields")
    
    print("                                          ")
    print("##########################################")
    print("###### Test Case #1: Product Search ######")
    for id in islice(ids, 0, 6, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")


    
    

   












# Call Method
test_abcXcendaDecisionMap ()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
##################### Xcenda Site Automation Decision Map Test Script ##########################
################################################################################################