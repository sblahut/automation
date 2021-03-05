    
    #import pytest
#import time
from datetime import datetime
#import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.webdriver.support import expected_conditions
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.support import expected_conditions as EC

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

# Open Domain
driver.get("https://www.starrcompanies.com/")
expectedURL = StarrEnvironmentLink

# Accept Cookies
driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click()  

def test_starrHomePage (testsPass,testsFail, testsWarning, testResult):

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click Report a Claim Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(2)").click()
    expectedURL = StarrEnvironmentLink + "Client-Services/Claims"

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

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Report a Claim Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Report a Claim Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Close Tab
    #driver.close()

    # Switch Back To First Tab
    #driver.switch_to.window(driver.window_handles[0])

    # Wait
    driver.implicitly_wait(15)

    # Print Results Of Test Script
    print("##########################################")
    print("####### Footer Links Test Results ########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                      END TEST CASE #9                                    #
    ############################################################################################
    
    ############################################################################################
    #                                   START TEST CASE #10                                    #
    ############################################################################################

    # Reset Page
    #driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click View All News Link
    driver.find_element(By.CSS_SELECTOR, "#content > div.newsfeed > div.newsfeed__view-all-container > div > a").click()
    expectedURL = StarrEnvironmentLink + "News"

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

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************View All News Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************View All News Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #10                                    #
    ############################################################################################

test_starrHomePage (testsPass,testsFail, testsWarning, testResult)