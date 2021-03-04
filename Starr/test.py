    
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

def test_starrHomePage (testsPass,testsFail, testsWarning, testResult):

    # Open Nav and navigate to International
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()

    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://international.starrlink.com/"

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
    print("****************International Link Results****************")
    print("URL Test Result: " + str(testResult))
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
    driver.close()

    # Switch Back To First Tab
    driver.switch_to.window(driver.window_handles[0])

    # Wait
    driver.implicitly_wait(15)
test_starrHomePage (testsPass,testsFail, testsWarning, testResult)