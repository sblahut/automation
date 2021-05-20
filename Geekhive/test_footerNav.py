################################################################################################
#################### Geekhive Site Automation Footer Links Test Script #########################
################################################################################################

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

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
#                                      START FOOTER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Get in Touch Link
driver.find_element(By.CSS_SELECTOR, ".btn-secondary:nth-child(2)").click()
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
print("****************Get in Touch Link Results*****************")
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

# Privacy Policy Link
driver.find_element(By.LINK_TEXT, "Privacy Policy").click()
expectedURL = GeekhiveEnvironmentLink + "privacy-policy"

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

    ############################################################################################
    #                                      END TEST CASE #2                                    #
    ############################################################################################
    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# About Link
driver.find_element(By.LINK_TEXT, "About").click()
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
print("*******************About Link Results*********************")
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

# Careers Link
driver.find_element(By.LINK_TEXT, "Careers").click()
expectedURL = GeekhiveEnvironmentLink + "careers"

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
    #                                      END TEST CASE #4                                    #
    ############################################################################################
    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Facebook Link
driver.find_element(By.CSS_SELECTOR, ".fa-facebook-f").click()
driver.switch_to.window(driver.window_handles[1])
ExternalLink = True
expectedURL = "https://www.facebook.com/geekhive"

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
print("******************Facebook Link Results*******************")
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

# Close Tab
driver.close()

# Switch Back To First Tab
driver.switch_to.window(driver.window_handles[0])

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

# Twitter Link
driver.find_element(By.CSS_SELECTOR, ".fa-twitter").click()
driver.switch_to.window(driver.window_handles[1])
ExternalLink = True
expectedURL = "https://twitter.com/geekhive"

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
print("*******************Twitter Link Results*******************")
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

# Close Tab
driver.close()

# Switch Back To First Tab
driver.switch_to.window(driver.window_handles[0])

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

# LinkedIn Link
driver.find_element(By.CSS_SELECTOR, ".fa-linkedin-in").click()
driver.switch_to.window(driver.window_handles[1])
ExternalLink = True
expectedURL = "https://www.linkedin.com/company/geekhive/"

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
print("******************LinkedIn Link Results*******************")
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

# Close Tab
driver.close()

# Switch Back To First Tab
driver.switch_to.window(driver.window_handles[0])

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

# Instagram Link
driver.find_element(By.CSS_SELECTOR, ".fa-instagram").click()
driver.switch_to.window(driver.window_handles[1])
ExternalLink = True
expectedURL = "https://www.instagram.com/geekhive/"

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
print("******************Instagram Link Results******************")
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

# Close Tab
driver.close()

# Switch Back To First Tab
driver.switch_to.window(driver.window_handles[0])

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

# Click Search Form in Footer
driver.find_element(By.CSS_SELECTOR, ".form-control").click()

# Type "Sitecore"
driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("Sitecore")

# Click Search Icon
driver.find_element(By.CSS_SELECTOR, ".fa-search").click()

expectedURL = GeekhiveEnvironmentLink + "search?keywords=Sitecore"

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
print("*******************Search Form Results********************")
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

