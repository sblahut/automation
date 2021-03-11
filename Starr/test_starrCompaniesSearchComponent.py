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
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
    
    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click()

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
    
    # Timestamp: Start Test
    testStart = datetime.now()

    expectedURL = StarrEnvironmentLink + "search?term=TRAVEL"

    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
        print("*****************Search Results: TRAVEL*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Search Results: TRAVEL*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Run results
    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        word = 'travel'

        contains_word = word in result.lower()
        
        if contains_word == False:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
        else:
            testsPass += 1
            break

    ############################################################################################
    #                                     END TEST CASE #1                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    # Switch to coverages
    driver.find_element(By.CSS_SELECTOR, "#content > div.search-results > div > div.search-results__rightrail > a:nth-child(3)").click()
    
    # Added wait to ensure results are updated
    time.sleep(2)
    
    # Run results
    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        word = 'travel'
        word2 = 'insurance'

        contains_words = word and word2 in result.lower()
        
        if contains_words == False:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
        else:
            testsPass += 1
            break

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #2                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click travel insurance link
    driver.find_element(By.CSS_SELECTOR, "#content > div.search-results > div > div.search-results__results-wrapper > div.search-results__results > a > div.search-results__result-title").click()
    
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"

    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
        print("*************Travel Insurance Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*************Travel Insurance Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Wait
    driver.implicitly_wait(15) 

    ############################################################################################
    #                                     END TEST CASE #3                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for GEEKHIVE....')
    search.send_keys('GEEKHIVE')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

    # Timestamp: Start Test
    testStart = datetime.now()

    expectedURL = StarrEnvironmentLink + "search?term=GEEKHIVE"

    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
        print("****************Search Results: GEEKHIVE******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Search Results: GEEKHIVE******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Run results
    ids = driver.find_elements_by_class_name('search-results__no-results-text')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        if result == 'No Results':
            testsPass += 1
            break
        else:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
    
    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #4                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for STARR INVESTMENT HOLDINGS....')
    search.send_keys('STARR INVESTMENT HOLDINGS')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

    # Timestamp: Start Test
    testStart = datetime.now()

    expectedURL = StarrEnvironmentLink + "search?term=STARR+INVESTMENT+HOLDINGS"

    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
        print("********Search Results: STARR INVESTMENT HOLDINGS*********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********Search Results: STARR INVESTMENT HOLDINGS*********")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Run results
    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        word = 'starr investment holdings'

        contains_word = word in result.lower()
        
        if contains_word == False:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
        else:
            testsPass += 1
            break
    
    # Wait
    driver.implicitly_wait(15)
        
    ############################################################################################
    #                                     END TEST CASE #5                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

    print('....Testing case sensitivity....')
    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for starr investment holdings....')
    search.send_keys('starr investment holdings')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()
    
    expectedURL = StarrEnvironmentLink + "search?term=starr+investment+holdings"

    # Running duplicate test to check for sensitivity in search functionality
    # Excluding normal speed test
    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

    if testResult == "Fail":
        print("********Search Results: STARR INVESTMENT HOLDINGS*********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    # Run results
    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):

        result = (str(id.text))
        
        word = 'starr investment holdings'

        contains_word = word in result.lower()
        
        if contains_word == False:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
        else:
            testsPass += 1
            break
    
    # Wait
    driver.implicitly_wait(15)
        
    ############################################################################################
    #                                     END TEST CASE #6                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #7                                    #
    ############################################################################################

    print('....Checking the ability to search for special charaters....')

    # Open search
    driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
    search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
    print('....Searching for !@#$%^....')
    search.send_keys('!@#$%^')
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

    # Timestamp: Start Test
    testStart = datetime.now()

    expectedURL = StarrEnvironmentLink + "search?term=%21%40%23%24%25%5E"

    if driver.current_url == expectedURL:
        testResult = "Pass"
        testsPass += 1
    else:
        testResult = "Fail"
        testsFail += 1

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
        print("******************Search Results: !@#$%^******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Search Results: !@#$%^******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Run results
    ids = driver.find_elements_by_class_name('search-results__result-title')

    for id in islice(ids, 0, 1, 1):
    
        result = (str(id.text))
        
        if result == 'No Results':
            testsPass += 1
            break
        else:
            print('ALERT: Search is not functioning correctly.')
            testsFail += 1
            break
    
    # Wait
    driver.implicitly_wait(15)
        
    ############################################################################################
    #                                     END TEST CASE #7                                     #
    ############################################################################################


    # Print Results Of Test Script
    print("                                          ")
    print("##########################################")
    print("########## Search Test Results ###########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")
    print("                                          ")
    
####################################################################################################
#                                       END SEARCH COMPONENT                                       #
####################################################################################################

test_starrHomePage (testsPass,testsFail, testsWarning, testResult)
test_searchHomepage (testsPass,testsFail, testsWarning, testResult)
    #Test is complete

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################