################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################

#import pytest
#import time
from datetime import datetime
#import json
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
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
    print("********************Homepage Results**********************")
    print("URL Test Result: " + str(testResult))
    print("Speed Test Result: " + str(speedTestResult))
    print(testNotes)
    print("**********************************************************")

####################################################################################################
#                                      START HEADER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

def test_headerNavLinks (testsPass,testsFail, testsWarning, testResult):
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
    print("*******************Logo Link Results**********************")
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
    print("*****************Careers Link Results*********************")
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
    print("***********Accident and Health Link Results***************")
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
    print("********Blanket Accident/Liability Link Results***********")
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
    print("************Business Accident Link Results****************")
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
    print("*********Group & Individual AD&D Link Results*************")
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
    print("*************Travel Insurance Link Results****************")
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
    print("************Aviation & Aerospace Link Results*************")
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
    print("********Commerical General Casualty Link Results**********")
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
    print("********Construction Primary & Excess Link Results*********")
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
    print("************Contractor Pollution Link Results*************")
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
    print("**************Crisis Management Link Results**************")
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
    print("********************Cyber Link Results********************")
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
    print("***************Defense Base Act Link Results**************")
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
    print("*******Energy Primary & Excess Casualty Link Results*******")
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
    print("****************Environmental Link Results****************")
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
    print("**********Federal-Employee-Liability Link Results*********")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(11) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Finance"

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
    print("****************Financial Lines Link Results**************")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(12) > a").click()
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
    print("****************Political Risk Link Results***************")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(13) > a").click()
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
    print("************Professional Liability Link Results***********")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(14) > a").click()
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
    print("*******Risk Management General Casualty Link Results******")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(15) > a").click()
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
    print("***************Site Pollution Link Results****************")
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
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(16) > a").click()
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
    print("**Workers Compensation & Employer Liability Link Results**")
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

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #23                                    #
    ############################################################################################

####################################################################################################
#                                        END HEADER LINKS                                          #
####################################################################################################

test_starrHomePage (testsPass,testsFail, testsWarning, testResult)
test_headerNavLinks (testsPass,testsFail, testsWarning, testResult)

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################