################################################################################################
######### American Society of Hematology Site Automation Site Explore Test Script ##############
################################################################################################

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

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
#                                      START Site Explore                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
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
    #                                      END TEST CASE #1                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

# Timestamp: Start Test
testStart = datetime.now()

# Click About Ash Link
driver.find_element(By.CSS_SELECTOR, ".crumbs > li:nth-child(2) > a").click()
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
print("******************About Ash Link Results******************")
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

# Click History Link
driver.find_element(By.CSS_SELECTOR, "#main-content > div.header-content__section > div > div.header-content__content-box.col-lg-9 > div > ul > li:nth-child(2) > a").click()
expectedURL = AshEnvironmentLink + "about/history"

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
print("******************History Link Results********************")
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

# Click Legends in Hematology Link
driver.find_element(By.CSS_SELECTOR, "#landingpage > div:nth-child(2) > div > div > div.row > div:nth-child(2) > h3 > a").click()
expectedURL = AshEnvironmentLink + "about/history/legends"

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
print("***********Legends In Hematology Link Results*************")
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

# Click Dirk van Bekkum Link
driver.find_element(By.CSS_SELECTOR, "#rightcolumnpage > div > div.col-md-9.left_content > div.container.people-gallery-container > div > div > div > div:nth-child(1) > p > a").click()
expectedURL = AshEnvironmentLink + "about/history/legends/dirk-van-bekkum-bio"

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
print("**************Dirk Van Bekkum Link Results****************")
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

# Click Dirk van Bekkum Link
driver.find_element(By.CSS_SELECTOR, "#main-content > div > div > div.col-md-9.left_content > div:nth-child(3) > div > div > ul > li:nth-child(2) > a").click()

# Wait For Cookie Alert
driver.implicitly_wait(15)

# Click Accept Cookies
driver.find_element_by_id("#onetrust-accept-btn-handler").click()
expectedURL = "https://www.nature.com/articles/bmt2015209"

if driver.current_url == expectedURL:
    testResult = "Pass"
else:
    testResult = "Fail"

# Timestamp: End Test
testEnd = datetime.now()

# Validation of Page Load Speed
testTime = (testEnd - testStart)
if testTime.seconds > expectedExternalPageLoadTimeInSeconds:
    speedTestResult = "Warning"
    testNotes = "Page load time is slow. Time: " + str(testTime)
else:
    speedTestResult = "Pass"
    testNotes = "Page load time is: " + str(testTime)

# Record Results
testTime = (testEnd - testStart)
print("**************Dirk Van Bekkum Link Results****************")
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

# Click Education Link
driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(2) > .nav-link").click()
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
print("*****************Education Link Results*******************")
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

# Click Focus On Dropdown Menu
driver.find_element(By.CSS_SELECTOR, "#dropdownMenuButton").click()

# Click On For Educators Link
driver.find_element(By.CSS_SELECTOR, "#main-content > div.header-content__section > div > div.header-content__focus-box.col-lg-3.landing-page-drop-list-container > div > div > div.row.justify-content-between > div:nth-child(1) > div > div > a:nth-child(3)").click()
expectedURL = AshEnvironmentLink + "education/educators"

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
print("*****************Educators Link Results*******************")
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

# Click Training Program Directors Link For Card Navigator  
driver.find_element(By.CSS_SELECTOR, "#a2115b19b-c3a3-455b-b75e-3bc93d06dd95 > div.card-sidebar > div.dropdown > div > button:nth-child(3) > h5").click()

# Click On Right Arrow For Card Navigator
driver.find_element(By.CSS_SELECTOR, "#cardNavigator_afc7b57a1-dd7a-45af-9aa3-49e5c02a1f5e > button.slick-arrow.slick-next > span.carousel-control-next-icon").click()

# Click On Learn More Link
driver.find_element(By.CSS_SELECTOR, "#cardNavigator_afc7b57a1-dd7a-45af-9aa3-49e5c02a1f5e > div > div > div:nth-child(4) > div > a > div > span").click()
expectedURL = AshEnvironmentLink + "education/educators/resources-for-training-program-directors/hematology-oncology-curricular-milestones"

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
print("*****************Educators Link Results*******************")
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
    #                                      END TEST CASE #9                                    #
    ############################################################################################





####################################################################################################
#                                       END Site Explore                                           #
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
######### American Society of Hematology Site Automation Site Explore Test Script ##############
################################################################################################