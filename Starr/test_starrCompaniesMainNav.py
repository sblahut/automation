################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
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
#                                      START HEADER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

def test_headerNavLinksProducts (testsPass,testsFail, testsWarning, testResult):
    print('....Checking Products Links....')

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click Logo Link
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()
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

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************Logo Link Results**********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Logo Link Results**********************")
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
    #                                      END TEST CASE #1                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click Careers Link
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__link > a").click()
    expectedURL = StarrEnvironmentLink + "Careers"

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
        print("*****************Careers Link Results*********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Careers Link Results*********************")
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
    #                                      END TEST CASE #2                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Accident and Health
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Accident-and-Health"

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
        print("***********Accident and Health Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***********Accident and Health Link Results***************")
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
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Blanket Accident/Liability & Special Risks
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Blanket-Accident"

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
        print("********Blanket Accident/Liability Link Results***********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********Blanket Accident/Liability Link Results***********")
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
    #                                      END TEST CASE #4                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Business Accident
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Business-Accident"

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
        print("************Business Accident Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Business Accident Link Results****************")
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
    #                                      END TEST CASE #5                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Group & Individual AD&D
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Group-and-Individual-AD-and-D"

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
        print("*********Group & Individual AD&D Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*********Group & Individual AD&D Link Results*************")
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
    #                                      END TEST CASE #6                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #7                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Travel Insurance
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"

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
        print("*************Travel Insurance Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*************Travel Insurance Link Results****************")
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
    #                                      END TEST CASE #7                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #8                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Aviation & Aerospace
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Aviation-and-Aerospace"

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
        print("************Aviation & Aerospace Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Aviation & Aerospace Link Results*************")
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
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Commerical General Casualty
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Commercial-General-Casualty"

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
        print("********Commerical General Casualty Link Results**********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********Commerical General Casualty Link Results**********")
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
    #                                      END TEST CASE #9                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #10                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Construction Primary & Excess
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Construction-Primary-and-Excess"

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
        print("********Construction Primary & Excess Link Results*********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********Construction Primary & Excess Link Results*********")
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

    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Contractor Pollution
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Contractor-Pollution"

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
        print("************Contractor Pollution Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Contractor Pollution Link Results*************")
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
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Crisis Management
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Crisis-Management"

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
        print("**************Crisis Management Link Results**************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**************Crisis Management Link Results**************")
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
    #                                     END TEST CASE #12                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Cyber
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Cyber"

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
        print("********************Cyber Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Cyber Link Results********************")
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
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Defense Base Act
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(6) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Defense-Base-Act"

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
        print("***************Defense Base Act Link Results**************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Defense Base Act Link Results**************")
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
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Energy Primary & Excess Casualty
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(7) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Energy-Primary-and-Excess-Casualty"

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
        print("*******Energy Primary & Excess Casualty Link Results*******")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******Energy Primary & Excess Casualty Link Results*******")
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
    #                                     END TEST CASE #15                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #16                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Environmental
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(8) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Environmental"

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
        print("****************Environmental Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Environmental Link Results****************")
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
    #                                     END TEST CASE #16                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #17                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Federal-Employee-Liability
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(9) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Federal-Employee-Liability"

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
        print("****************Environmental Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Environmental Link Results****************")
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
    #                                     END TEST CASE #17                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #18                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Financial Lines
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(10) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Finance"

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
        print("****************Financial Lines Link Results**************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Financial Lines Link Results**************")
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
    #                                     END TEST CASE #18                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #19                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Political Risk
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(11) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Political-Risk"

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
        print("****************Political Risk Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Political Risk Link Results***************")
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
    #                                     END TEST CASE #19                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #20                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Professional Liability
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(12) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Professional-Liability"

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
        print("************Professional Liability Link Results***********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Professional Liability Link Results***********")
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
    #                                     END TEST CASE #20                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #21                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Risk Management General Casualty
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(13) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Risk-Management-General-Casualty"

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
        print("*******Risk Management General Casualty Link Results******")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******Risk Management General Casualty Link Results******")
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
    #                                     END TEST CASE #21                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #22                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Site Pollution
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(14) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Site-Pollution"

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
        print("***************Site Pollution Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Site Pollution Link Results****************")
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
    #                                     END TEST CASE #22                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #23                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Workers Compensation & Employer Liability
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(15) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Workers-Compensation-and-Employer-Liability"

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
        print("**Workers Compensation & Employer Liability Link Results**")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**Workers Compensation & Employer Liability Link Results**")
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
    #                                     END TEST CASE #23                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #24                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Inland Marine
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"

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
        print("****************Inland Marine Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Inland Marine Link Results****************")
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
    #                                     END TEST CASE #24                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #25                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Marine
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Marine/Marine"

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
        print("*******************Marine Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Marine Link Results********************")
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
    #                                     END TEST CASE #25                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #26                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to General Property
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/General-Property"

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
        print("**************General Property Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**************General Property Link Results***************")
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
    #                                     END TEST CASE #26                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #27                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Energy - Technical Risks
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Energy---Technical-Risks"

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
        print("***************Technical Risks Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Technical Risks Link Results***************")
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
    #                                     END TEST CASE #27                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #28                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Construction - Builders Risk
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Construction---Builders-Risk"

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
        print("*****************Builders Risk Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Builders Risk Link Results***************")
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
    #                                     END TEST CASE #28                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #29                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Inland Marine
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"

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
        print("*****************Inland Marine Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Inland Marine Link Results***************")
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

    # Print Results Of Test Script
    print("##########################################")
    print("########## Products Test Results #########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                     END TEST CASE #29                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #30                                   #
    ############################################################################################

def test_headerNavLinksIndustry (testsPass,testsFail, testsWarning, testResult):
    print('....Checking Industry Links....')

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Aviation & Aerospace
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Aviation-and-Aerospace"

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
        print("************Aviation & Aerospace Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Aviation & Aerospace Link Results*************")
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
    #                                      END TEST CASE #30                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #31                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Business Travel
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Business-Accident"

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
        print("**************Business Travel Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**************Business Travel Link Results****************")
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
    #                                      END TEST CASE #31                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #32                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Construction
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Construction"

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
        print("****************Construction Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Construction Link Results*****************")
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
    #                                      END TEST CASE #32                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #33                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Energy
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Energy"

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
        print("*******************Energy Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Energy Link Results********************")
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
    #                                      END TEST CASE #33                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #34                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Environmental
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Environmental"

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
        print("****************Environmental Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Environmental Link Results****************")
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
    #                                      END TEST CASE #34                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #35                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Food & Beverage
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(6) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Food-and-Beverage"

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
        print("***************Food & Beverage Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Food & Beverage Link Results***************")
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
    #                                      END TEST CASE #35                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #36                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Government Contractors
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(7) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Defense-Base-Act"

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
        print("***********Government Contractors Link Results************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***********Government Contractors Link Results************")
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
    #                                      END TEST CASE #36                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #37                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Hospitality
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(8) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Hospitality"

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
        print("****************Hospitality Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Hospitality Link Results******************")
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
    #                                      END TEST CASE #37                                   #
    ############################################################################################
    
    ############################################################################################
    #                                    START TEST CASE #38                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Manufacturing
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(9) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Manufacturing"

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
        print("****************Manufacturing Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Manufacturing Link Results****************")
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
    #                                      END TEST CASE #38                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #39                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Marine
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(10) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Marine/Marine"

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
        print("********************Marine Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Marine Link Results*******************")
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
    #                                      END TEST CASE #39                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #40                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Real Estate
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(11) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Real-Estate"

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
        print("*****************Real Estate Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Real Estate Link Results*****************")
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
    #                                      END TEST CASE #40                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #41                                   #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open Nav and navigate to Retail
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(12) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Retail"

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
        print("********************Retail Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Retail Link Results*******************")
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
    #                                      END TEST CASE #42                                   #
    ############################################################################################

    # Open Nav and navigate to Travel
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
    outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(13) > a"
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
    driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"

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
        print("********************Travel Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Travel Link Results*******************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #42                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #43                                   #
    ############################################################################################

    # Open Nav and navigate to View All
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(3) > a").click()  
    expectedURL = StarrEnvironmentLink + "Insurance/View-All"

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
        print("*******************View All Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************View All Link Results******************")
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

    # Print Results Of Test Script
    print("##########################################")
    print("########## Industry Test Results #########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                      END TEST CASE #43                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #44                                   #
    ############################################################################################

def test_headerNavLinksRemainder (testsPass,testsFail, testsWarning, testResult):
    print('....Checking Remaining Nav Links....')

    # Open Nav and navigate to Become a Starr Agent/Broker
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(1) > a").click()  
    expectedURL = StarrEnvironmentLink + "Agents"

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
        print("**************Starr Agent/Broker Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**************Starr Agent/Broker Link Results*************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #44                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #45                                   #
    ############################################################################################

    # Open Nav and navigate to Domestic
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
    driver.implicitly_wait(300)
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://www.starrlink.com/"

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
        print("*******************Domestic Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Domestic Link Results******************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()
    
    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #45                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #46                                   #
    ############################################################################################

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

    if testResult == "Fail":
        print("****************International Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************International Link Results****************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #46                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #47                                   #
    ############################################################################################

    # Open Nav and navigate to Star Assist
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(3) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://travelagencies.starrassist.com/"

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
        print("*****************Star Assist Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Star Assist Link Results*****************")
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

    ############################################################################################
    #                                      END TEST CASE #47                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #48                                   #
    ############################################################################################

    # Open Nav and navigate to Global Offices
    driver.find_element(By.CSS_SELECTOR, "#link-group-2 > a").click()
    expectedURL = StarrEnvironmentLink + "Global-Reach"

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
        print("*****************Global Reach Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Global Reach Link Results****************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #48                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #49                                   #
    ############################################################################################

    # Open Nav and navigate to Who We Are
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Who-We-Are"

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
        print("******************Who We Are Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Who We Are Link Results*****************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #49                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #50                                   #
    ############################################################################################

    # Open Nav and navigate to History
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "About/History"

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
        print("*******************History Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************History Link Results*******************")
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
    #                                      END TEST CASE #50                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #51                                   #
    ############################################################################################

    # Open Nav and navigate to Leadership
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Leadership"

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
        print("******************Leadership Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Leadership Link Results*****************")
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
    #                                      END TEST CASE #51                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #52                                   #
    ############################################################################################

    # Open Nav and navigate to Leadership
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Investments"

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
        print("*****************Investments Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Investments Link Results*****************")
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
    #                                      END TEST CASE #52                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #53                                   #
    ############################################################################################

    # Open Nav and navigate to Client Services
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Client-Services"

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
        print("***************Client Services Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Client Services Link Results***************")
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
    #                                      END TEST CASE #53                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #54                                   #
    ############################################################################################

    # Open Nav and navigate to Contact Us
    driver.find_element(By.CSS_SELECTOR, "#link-group-4 > a").click()
    expectedURL = StarrEnvironmentLink + "Contact-Us"

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
        print("******************Contact Us Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Contact Us Link Results*****************")
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
    #                                      END TEST CASE #54                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #55                                   #
    ############################################################################################

    # Open Nav and navigate to News
    driver.find_element(By.CSS_SELECTOR, "#link-group-5 > a").click()
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
        print("*********************News Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*********************News Link Results********************")
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
    #                                      END TEST CASE #55                                   #
    ############################################################################################

    # Print Results Of Test Script
    print("##########################################")
    print("######### Remainder Test Results #########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")
    
####################################################################################################
#                                        END HEADER LINKS                                          #
####################################################################################################

test_starrHomePage (testsPass,testsFail, testsWarning, testResult)
test_headerNavLinksProducts (testsPass,testsFail, testsWarning, testResult)
test_headerNavLinksIndustry (testsPass,testsFail, testsWarning, testResult)
test_headerNavLinksRemainder (testsPass,testsFail, testsWarning, testResult)

    #Test is complete

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################