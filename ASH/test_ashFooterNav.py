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
AshEnvironmentLink = "https://www.hematology.org/"

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
print("********************Homepage Results**********************")
print("URL Test Result: " + str(testResult))
print("Speed Test Result: " + str(speedTestResult))
print(testNotes)
print("**********************************************************")

# Set Window Size
driver.maximize_window()

# Wait
time.sleep(1)

#Scroll Down To Footer
driver.execute_script("window.scrollTo(0, window.scrollY + 9999)")

####################################################################################################
#                                      START FOOTER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click Facebook Link
driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(1)").click()
expectedURL = "https://www.facebook.com/AmericanSocietyofHematology"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedExternalPageLoadTimeInSeconds: # 5 Seconds for external link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("*****************Facebook Link Results********************")
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

# Go back to the previous page
driver.back()

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

# Click LinkedIn Link
driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(2)").click()
expectedURL = "https://www.linkedin.com/company/american-society-of-hematology"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedExternalPageLoadTimeInSeconds: # 5 Seconds for external link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("*****************LinkedIn Link Results********************")
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

# Go back to the previous page
driver.back()

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

# Click Twitter Link
driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(3)").click()
expectedURL = "https://twitter.com/ASH_hematology"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedExternalPageLoadTimeInSeconds: # 5 Seconds for external link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("******************Twitter Link Results********************")
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

# Go back to the previous page
driver.back()

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

# Click YouTube Link
driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(4)").click()
expectedURL = "https://www.youtube.com/user/ASHWebmaster"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedExternalPageLoadTimeInSeconds: # 5 Seconds for external link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("******************YouTube Link Results********************")
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

# Go back to the previous page
driver.back()

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

# Click Support Opportunities Link
driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(1)").click()
expectedURL = AshEnvironmentLink + "about/corporate-support"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedPageLoadTimeInSeconds: # 3 Seconds for internal link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("***********Support Opportunities Link Results*************")
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

#Scroll Down To Footer
driver.execute_script("window.scrollTo(0, window.scrollY + 9999)")

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

# Click Privacy Policy Link
driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(2)").click()
expectedURL = AshEnvironmentLink + "about/privacy-policy"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedPageLoadTimeInSeconds: # 3 Seconds for internal link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("***************Privacy Policy Link Results****************")
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

#Scroll Down To Footer
driver.execute_script("window.scrollTo(0, window.scrollY + 9999)")

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

# Click Terms of Service Link
driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(3)").click()
expectedURL = AshEnvironmentLink + "about/terms-of-service"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedPageLoadTimeInSeconds: # 3 Seconds for internal link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("**************Terms of Service Link Results***************")
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

#Scroll Down To Footer
driver.execute_script("window.scrollTo(0, window.scrollY + 9999)")

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

# Click Contact Us Link
driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(4)").click()
expectedURL = AshEnvironmentLink + "contact-us"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedPageLoadTimeInSeconds: # 3 Seconds for internal link
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("*****************Contact Us Link Results******************")
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



####################################################################################################
#                                        END FOOTER LINKS                                          #
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
######### American Society of Hematology Site Automation Footer Links Test Script ##############
################################################################################################