################################################################################################
############## American Society of Hematology Site Automation Account Login Script #############
################################################################################################

import pytest
import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver = webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

testResult = ""

def test_ashLogin():

    # Username & Password storage
    username = "002fa@pprodloadtest.com"
    password = "Ash2020!"

    # Results declaration
    testResult = ""
    expectedPageLoadTimeInSeconds = 5
    domain = "https://hematology.org/"

    # Record Script Start Time for Script Duration
    scriptStart = datetime.now()

    print('....Navigating to www.hematology.org/....')
    
    # Open ash website
    driver.get(domain)

    # Click my account icon on homepage 
    driver.find_element(By.CSS_SELECTOR, ".my-account__icon").click()
    
    # Sign in button declaration
    element = driver.find_element(By.CSS_SELECTOR, "#okta-signin-submit")

    # Click on username field
    driver.find_element(By.ID, "okta-signin-username").click()

    # Type username
    driver.find_element(By.ID, "okta-signin-username").send_keys("", username)

    # Wait
    time.sleep(2)

    # Click on password field
    driver.find_element(By.ID, "okta-signin-password").click()

    # Type password
    driver.find_element(By.ID, "okta-signin-password").send_keys("", password)

    # Wait
    time.sleep(2)

    # Check privacy box
    driver.find_element(By.ID, "privacyCheckbox").click()

    # Wait
    time.sleep(2)

    # Check terms and conditions box
    driver.find_element(By.ID, "termsCheckbox").click()

    # Wait
    time.sleep(2)
    
    print('....Signing into https://sso.hematology.org/ now....')

    # Timestamp: Start Test
    testStart = datetime.now()

    # Submit login
    (element).click()

    # Wait for login successful login attempt
    time.sleep(10)

    # Check to see if login was successful
    try:
        loginSelector = driver.find_element_by_class_name('nav-item__my-account-name')
        if loginSelector.is_displayed():
            testResult = "Pass"
    except NoSuchElementException:
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
    print("                                         ")
    print("############# Login Results #############")
    if testResult == "Fail":
        print("Username Failed: " + str(username))
    print("Login Test Result: " + str(testResult))
    print("Speed Test Result: " + str(speedTestResult))
    print(testNotes)
    print("#########################################")
    print("                                         ") 

    if testResult == "Fail":
        print("#########################################")
        print("############# Login Failed! #############")
        print("#########################################")
        print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
        print("#########################################")
        print("                                         ")
    else:
        print("#########################################")
        print("############ Login Success! #############")
        print("#########################################")
        print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
        print("#########################################")
        print("                                         ")

# Call Method ashLogin
test_ashLogin()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  


################################################################################################
############## American Society of Hematology Site Automation Account Login Script #############
################################################################################################