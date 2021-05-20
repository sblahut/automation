################################################################################################
############### World Courier Site Automation Insights Filter Test Script ######################
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

def test_abcWorldCourierInsightsFilter():

    print('....Navigating to www.worldcourier.com/insights....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Filter Functionality ######')
    
    # Open wc website
    driver.get('https://www.worldcourier.com/insights')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()
    
    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.marginator.margin-top-2 > form > span:nth-child(2) > label > select").click()

    # Click A-Z
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.marginator.margin-top-2 > form > span:nth-child(2) > label > select > option:nth-child(3)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__title')
    print("                                          ")
    print("##########################################")
    print("############## Results A-Z ###############")
    for id in islice(ids, 0, 10, 1):        
        print("Class: " + str(id.text))
    print("##########################################")
    print("                                          ")
    
    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.marginator.margin-top-2 > form > span:nth-child(2) > label > select").click()

    # Click Z-A
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__middle > div.marginator.margin-top-2 > form > span:nth-child(2) > label > select > option:nth-child(4)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__title')
    
    print("                                          ")
    print("##########################################")
    print("############## Results Z-A ###############")
    for id in islice(ids, 0, 10, 1):            
        print("Class: " + str(id.text))
    print("##########################################")
    print("                                          ")

# Call Method
test_abcWorldCourierInsightsFilter()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
############### World Courier Site Automation Insights Filter Test Script ######################
################################################################################################