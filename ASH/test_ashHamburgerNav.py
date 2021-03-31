################################################################################################
########## American Society of Hematology Site Automation Hamburger Links Test Script ##########
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
AshEnvironmentLink = "https://www.hematology.org/"

# Expected Page Load Time
expectedPageLoadTimeInSeconds = 3

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
print("....Navigating to the American Society of Hematology webpage...")

# Open Geekhive Site
driver.get("https://www.hematology.org/")
expectedURL = AshEnvironmentLink

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

if testResult == "Fail":
    print("********************Homepage Results**********************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("********************Homepage Results**********************")
    print("Speed Test Result: " + str(speedTestResult))
    print(testNotes)
    print("**********************************************************")

# Set Window Size
driver.set_window_size(1400, 1214)

####################################################################################################
#                                     START HAMBURGER LINKS                                        #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Research Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(1) > .nav-link").click()
expectedURL = AshEnvironmentLink + "research"

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
    print("******************Research Link Results*******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("******************Research Link Results*******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Education Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(2) > .nav-link").click()
expectedURL = AshEnvironmentLink + "education"

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
    print("******************Education Link Results******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("******************Education Link Results******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Advocacy Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(3) > .nav-link").click()
expectedURL = AshEnvironmentLink + "advocacy"

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
    print("*******************Advocacy Link Results******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("*******************Advocacy Link Results******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Careers Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(4) > .nav-link").click()
expectedURL = AshEnvironmentLink + "about/careers"

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
    print("*******************Careers Link Results*******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("*******************Careers Link Results*******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Meetings Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(5) > .nav-link").click()
expectedURL = AshEnvironmentLink + "meetings"

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
    print("******************Meetings Link Results*******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("******************Meetings Link Results*******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Publications Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(6) > .nav-link").click()
expectedURL = AshEnvironmentLink + "publications"

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
    print("****************Publications Link Results*****************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("****************Publications Link Results*****************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Awards Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(7) > .nav-link").click()
expectedURL = AshEnvironmentLink + "awards"

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
    print("*******************Awards Link Results********************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("*******************Awards Link Results********************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Newsroom Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__blue-section .nav-item:nth-child(8) > .nav-link").click()
expectedURL = AshEnvironmentLink + "newsroom"

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
    print("******************Newsroom Link Results*******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("******************Newsroom Link Results*******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click About Ash Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__white-section .nav-item:nth-child(1) > .nav-link").click()
expectedURL = AshEnvironmentLink + "about"

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
    print("******************About Ash Link Results******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("******************About Ash Link Results******************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click Ash Foundation Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__white-section .nav-item:nth-child(2) > .nav-link").click()
expectedURL = AshEnvironmentLink + "foundation"

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
    print("***************Ash Foundation Link Results****************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("***************Ash Foundation Link Results****************")
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

# Toggle Hamburger Menu
driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()

# Click My Account Link
driver.find_element(By.CSS_SELECTOR, ".side-menu-container__white-section .nav-item:nth-child(3) > .nav-link").click()
expectedURL = "https://sso.hematology.org/?_ga=2.148013492.284796152.1610484732-1033274404.1610124680"

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
    print("*****************My Account Link Results******************")
    print("URL Test Result: " + str(testResult))
    print("**********************************************************")

if speedTestResult == "Warning":
    print("*****************My Account Link Results******************")
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


####################################################################################################
#                                      END HAMBURGER LINKS                                         #
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


################################################################################################
########## American Society of Hematology Site Automation Hamburger Links Test Script ##########
################################################################################################