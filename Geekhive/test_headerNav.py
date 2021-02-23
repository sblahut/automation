################################################################################################
#################### Geekhive Site Automation Header Links Test Script #########################
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
GeekhiveEnvironmentLink = "https://www.geekhive.com/"

# Expected Page Load Time
expectedPageLoadTimeInSeconds = 3

# Declaration of Wait Time

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
print("....Navigating to the Geekhive webpage...")

# Open Geekhive Site
driver.get("https://www.geekhive.com/")
expectedURL = GeekhiveEnvironmentLink

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
driver.set_window_size(1400, 1214)

####################################################################################################
#                                      START HEADER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Logo Link
driver.find_element(By.CSS_SELECTOR, ".navbar-brand > svg").click()
expectedURL = GeekhiveEnvironmentLink

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
print("*******************Logo Link Results**********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #1                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Services Link
driver.find_element(By.CSS_SELECTOR, ".has-children:nth-child(1) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "services"

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
print("*****************Services Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #2                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over Services
element = driver.find_element(By.CSS_SELECTOR, ".has-children:nth-child(1) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
    
# Click Customer Experience Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(1) .menu-item:nth-child(1) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "services/customer-experience"

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
print("************Customer Experience Link Results**************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over Services
element = driver.find_element(By.CSS_SELECTOR, ".has-children:nth-child(1) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Click Data, Analytics & Visualization Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(1) .menu-item:nth-child(2) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "services/data-analytics-visualization"

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
print("***************Data & Visual Link Results*****************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #4                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over Services
element = driver.find_element(By.CSS_SELECTOR, ".has-children:nth-child(1) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
   
# Click Content Marketing Link
driver.find_element(By.CSS_SELECTOR, ".navbar-dropdown > .menu-item:nth-child(3) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "services/content-marketing"

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
print("*************Content Marketing Link Results***************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #5                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over Services
element = driver.find_element(By.CSS_SELECTOR, ".has-children:nth-child(1) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

# Click Technology Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(4) > .btn").click()
expectedURL = GeekhiveEnvironmentLink + "services/technology"

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
print("****************Technology Link Results*******************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #6                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #7                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Industries Link
driver.find_element(By.CSS_SELECTOR, ".navbar-nav > .menu-item:nth-child(2) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "industries"

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
print("****************Industries Link Results*******************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #7                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #8                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Thinking Link
driver.find_element(By.CSS_SELECTOR, ".navbar-nav > .menu-item:nth-child(3) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "thinking"

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
print("*****************Thinking Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Work Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(4) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "work"

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
print("*******************Work Link Results**********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #9                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #10                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Partners Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(5) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "partners"

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
print("*****************Partners Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #10                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over About
element = driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(6) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
   
# Click Company Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(6) .menu-item:nth-child(1) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "about"

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
print("******************Company Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over About
element = driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(6) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
    
# Click Events Link
driver.find_element(By.CSS_SELECTOR, ".menu-item--active-trail .menu-item:nth-child(2) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "events"

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
print("******************Events Link Results*********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #12                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Mouse Over About
element = driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(6) > .menu-item-link")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
## WAIT ##

# Click Press Releases Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(3) > .btn").click()
expectedURL = GeekhiveEnvironmentLink + "press-releases"

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
print("**************Press Releases Link Results*****************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Careers Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(7) > .menu-item-link").click()
expectedURL = GeekhiveEnvironmentLink + "careers"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Click View Open Positions Link
driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(1)").click()

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
print("******************Careers Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1

# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Contact Link
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(8) > .btn").click()
expectedURL = GeekhiveEnvironmentLink + "contact"

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
print("******************Contact Link Results********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Record Results To Tally For Final Results
if testResult == "Pass":
    TestsPass += 1
elif testResult == "Fail":
    TestsFail += 1
elif testResult == "Warning":
    TestsWarning += 1

if speedTestResult == "Pass":
    TestsPass += 1
elif speedTestResult == "Fail":
    TestsFail += 1
elif speedTestResult == "Warning":
    TestsWarning += 1
    
# Wait
driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #15                                    #
    ############################################################################################

####################################################################################################
#                                        END HEADER LINKS                                          #
####################################################################################################

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