################################################################################################
################# Starr Companies Site Automation Search Component Test Script #################
################################################################################################

import time
import requests
from itertools import islice
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Main Domain Link
StarrEnvironmentLink = "https://www.starrcompanies.com/"

# Expected Page Load Time
expectedPageLoadTimeInSeconds = 3

# Results Declaration
testsPass = 0
testsFail = 0
testsWarning = 0
testResult = ""

# Record Script Start Time for Script Duration
scriptStart = datetime.now()

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

# Wait
driver.implicitly_wait(15)

# Timestamp: Start Test
testStart = datetime.now()

# Loading message
print("....Navigating to the Starr Companies homepage...")

def test_starrHomePage (testsPass,testsFail, testsWarning, testResult):

        # Open Domain
    driver.get("https://www.starrcompanies.com/")
    expectedURL = StarrEnvironmentLink

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results To Tally For Final Results
    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("********************Homepage Results**********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Homepage Results**********************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

####################################################################################################
#                                      START SEARCH COMPONENT                                      #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

def test_searchHomepage (testsPass,testsFail, testsWarning, testResult):
    print('....Opening Search....')

    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for TRAVEL....')
    search.send_keys('TRAVEL')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        word = 'travel'

        contains_word = word in result.lower()
        
        if contains_word == False:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
        else:
            testsPass += 1
        
    ############################################################################################
    #                                     END TEST CASE #1                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for GEEKHIVE....')
    search.send_keys('GEEKHIVE')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

    ids = driver.find_elements_by_class_name('search-results__no-results-text')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        if result == 'No Results':
            testsPass += 1
        else:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
        
    ############################################################################################
    #                                     END TEST CASE #2                                     #
    ############################################################################################



    # Print Results Of Test Script
    #print("##########################################")
    #print("########## Search Test Results ###########")
    #print("##########################################")
    #print("Number of Pass Results: " + str(testsPass))
    #print("Number of Fail Results: " + str(testsFail))
    #print("Number of Warnings: " + str(testsWarning))
    #print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    #print("##########################################")
    print("############## Test Complete #############")
    #print("##########################################")
    
####################################################################################################
#                                       END SEARCH COMPONENT                                       #
####################################################################################################

test_starrHomePage (testsPass,testsFail, testsWarning, testResult)
test_searchHomepage (testsPass,testsFail, testsWarning, testResult)
    #Test is complete

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################