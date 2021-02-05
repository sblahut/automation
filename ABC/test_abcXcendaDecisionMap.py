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
    
    print('....Navigating to www.xcenda.com/decision-map....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Filter Functionality ######')
    # Open xcenda website
    driver.get('https://www.xcenda.com/decision-map')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

    print('....Filtering by Product....')

    # Click product dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(1) > label > dl > dt > a").click()

    # Select '5-aminolevulinic acid'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(1) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Run Results
    ids = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > div")
    
    print("                                          ")
    print("##########################################")
    print("########## Test Case #1: Product #########")
    for id in islice(ids, 0, 1, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Unselect '5-aminolevulinic acid'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(1) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Wait
    time.sleep(2)

    print('....Filtering by Therapeutic Area....')

   # Click therapeutic area dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(2) > label > dl > dt > a").click()

    # Select 'acromegaly'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(2) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Run Results
    ids = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > div")
   
    print("                                          ")
    print("##########################################")
    print("###### Test Case #2: Therapeudic Area #####")
    for id in islice(ids, 0, 1, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Unselect 'acromegaly'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(2) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Wait
    time.sleep(2)

    print('....Filtering by Country....')

   # Click country dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(3) > label > dl > dt > a").click()

    # Select 'Australia'
    driver.find_element(By.CSS_SELECTOR, "#Australia\ \(PBAC\)").click()

    # Run Results
    ids = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > div")
   
    print("                                          ")
    print("##########################################")
    print("########## Test Case #3: Country #########")
    for id in islice(ids, 0, 1, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Unselect 'Australia'
    driver.find_element(By.CSS_SELECTOR, "#Australia\ \(PBAC\)").click()

    # Wait
    time.sleep(2)

    print('....Filtering by Year....')

   # Click year dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(4) > label > dl > dt > a").click()

    # Select '2012'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(4) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Run Results
    ids = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > div")
 
    print("                                          ")
    print("##########################################")
    print("########### Test Case #4: Year ###########")
    for id in islice(ids, 0, 1, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Unselect '2012'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(4) > label > dl > dd > div > ul > li:nth-child(1) > label").click()

    # Wait
    time.sleep(2)

    print('....Filtering by Decision....')

   # Click decision dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div:nth-child(1) > div > div > div > form > div:nth-child(5) > label > dl > dt > a").click()

    # Select 'favorable'
    driver.find_element(By.CSS_SELECTOR, "#Favorable").click()

    # Run Results
    ids = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > div")
 
    print("                                          ")
    print("##########################################")
    print("######### Test Case #5: Decision #########")
    for id in islice(ids, 0, 1, 1):
        
        print("First Result: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Unselect 'favorable'
    driver.find_element(By.CSS_SELECTOR, "#Favorable").click()

    # Wait
    time.sleep(2)

    print('....Sorting by Year....')

   # Click sort by dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select").click()

    # Select 'year'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(2)").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "card-body")

    print("                                          ")
    print("##########################################")
    print("###### Test Case #6: Sort By: Year #######")
    for id in islice(ids, 0, 3, 1):
        print("                                          ")
        print("First Three Result(s): " + str(id.text))
        print("                                          ")
    print("##########################################")
    print("                                          ")

    # Unselect 'year'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(2)").click()

    # Wait
    time.sleep(2)

    print('....Sorting by Country....')

   # Click sort by dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select").click()

    # Select 'country'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(3)").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "card-body")

    print("                                          ")
    print("##########################################")
    print("##### Test Case #7: Sort By: Country #####")
    for id in islice(ids, 0, 3, 1):
        print("                                          ")
        print("First Three Result(s): " + str(id.text))
        print("                                          ")
    print("##########################################")
    print("                                          ")

    # Unselect 'country'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(3)").click()

    # Wait
    time.sleep(2)

    print('....Sorting by Decision....')

   # Click sort by dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select").click()

    # Select 'decision'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(4)").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "card-body")

    print("                                          ")
    print("##########################################")
    print("#### Test Case #8: Sort By: Decision #####")
    for id in islice(ids, 0, 3, 1):
        print("                                          ")
        print("First Three Result(s): " + str(id.text))
        print("                                          ")
    print("##########################################")
    print("                                          ")

    # Unselect 'decision'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(4)").click()

    # Wait
    time.sleep(2)

    print('....Sorting by Therapeutic Area....')

   # Click sort by dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select").click()

    # Select 'therapeutic area'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(5)").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "card-body")

    print("                                          ")
    print("##########################################")
    print("##### Test Case #9: Sort By: T. Area #####")
    for id in islice(ids, 0, 3, 1):
        print("                                          ")
        print("First Three Result(s): " + str(id.text))
        print("                                          ")
    print("##########################################")
    print("                                          ")

    # Unselect 'therapeutic area'
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div:nth-child(3) > div > div.decision-card-list > div.container > div > div > div > div > span:nth-child(1) > label > span.filter__form-item__control > div > select > option:nth-child(5)").click()

    # Wait
    time.sleep(2)



# Call Method
test_abcXcendaDecisionMap ()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
##################### Xcenda Site Automation Decision Map Test Script ##########################
##############################################################################################