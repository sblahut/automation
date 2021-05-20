################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
################################################################################################

import datetime
from itertools import islice
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Declare Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

scriptStart = datetime.datetime.now()

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
    print('....Searching for Seattle....')
    print("                                          ")
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.location-finder > div.location-finder-search-wrapper.background-true-blue > div > div > div > form > div > button.location-finder-search__button").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "location-card__address")
    
    print("                                          ")
    print("##########################################")
    print("########## Test Case #1: Seattle #########")
    for id in islice(ids, 0, 3, 1):
        
        print("Address: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Search 'Central'
    search.clear()
    search.send_keys("Central")
    print('....Searching for Central Region....')
    print("                                          ")
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.location-finder > div.location-finder-search-wrapper.background-true-blue > div > div > div > form > div > button.location-finder-search__button").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "location-card__address")
    
    print("                                          ")
    print("##########################################")
    print("########## Test Case #2: Central #########")
    for id in islice(ids, 0, 3, 1):
        
        print("Address: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Search '98101'
    search.clear()
    search.send_keys("98101")
    print('....Searching for 98101 Zip Code....')
    print("                                          ")
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.location-finder > div.location-finder-search-wrapper.background-true-blue > div > div > div > form > div > button.location-finder-search__button").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "location-card__address")
    
    print("                                          ")
    print("##########################################")
    print("########## Test Case #3: 98101 ##########")
    for id in islice(ids, 0, 3, 1):
        
        print("Address: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Search 'Current Location'
    search.clear()
    print('....Searching by Current Location....')
    print("                                          ")
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.location-finder > div.location-finder-search-wrapper.background-true-blue > div > div > div > form > div > button.location-finder-search__button--location").click()

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "location-card__address")
    
    print("                                          ")
    print("##########################################")
    print("##### Test Case #4: Current Location #####")
    for id in islice(ids, 0, 3, 1):
        
        print("Address: " + str(id.text))
    print("##########################################")
    print("                                          ")

# Call Method
test_abcInnomarClinicLocator ()

print("##########################################")
print("############## Test Complete #############")
print("Total Run Time of Script: " + str(datetime.datetime.now() - scriptStart))
print("##########################################")
print("                                          ")

#Test is complete
driver.quit()  

################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
################################################################################################