################################################################################################
######### American Society of Hematology Site Automation Footer Links Test Script ##############
################################################################################################

import pytest
import time
from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

# Main Domain Link
StarrEnvironmentLink = "https://starrwright-qa.starr.ghclients.com/"

# Expected Page Load Time
expectedPageLoadTimeInSeconds = 3
expectedExternalPageLoadTimeInSeconds = 5

# Results Declaration
TestsPass = 0
TestsFail = 0
TestsWarning = 0
testResult = ""

# Record Script Start Time for Script Duration
scriptStart = datetime.now()

# Declare Chrome Driver
driver = webdriver.Chrome("./chromedriver")

# Wait
driver.implicitly_wait(15)

# Timestamp: Start Test
testStart = datetime.now()

# Loading message
print("....Navigating to the Starr Wright USA webpage...")

# Open Geekhive Site
driver.get("https://starrwright-qa.starr.ghclients.com/")
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
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Record Results
testTime = (testEnd - testStart)
print("********************Homepage Results**********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Set Window Size
driver.maximize_window()

# Wait
time.sleep(1)

# Toggle Search
driver.find_element(By.CSS_SELECTOR, "#search-toggle").click()

# Send Example Query
element = driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input").send_keys("Travel Insurance")

driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input") == driver.switchTo().active_element






    


# Print Results Of Test Script
print("##########################################")
print("########### Overall Test Results #########")
print("##########################################")
print("Number of Pass Results: " + str(TestsPass))
print("Number of Fail Results: " + str(TestsFail))
print("Number of Warnings: " + str(TestsWarning))
print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
print("##########################################")
print("############## Test Complete #############")
print("##########################################")
time.sleep(1)
#Test is complete
driver.quit()

################################################################################################
######### American Society of Hematology Site Automation Header Links Test Script ##############
################################################################################################