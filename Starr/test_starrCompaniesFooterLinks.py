################################################################################################
################ Starr Companies Site Automation Footer Links Test Script ######################
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

def test_starrHomePage (testsPass, testsFail, testsWarning, testResult):

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

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click()  

####################################################################################################
#                                      START FOOTER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

def test_starrFooterLinks (testsPass, testsFail, testsWarning, testResult):
    print('....Checking Footer Links....')

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click Logo Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__logo > a > img").click()
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
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(1) > a").click()
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
        print("******************Careers Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Careers Link Results********************")
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

    # Click Confidentiality Protocol Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Confidentiality-Protocol"

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
        print("**********Confidentiality Protocol Link Results***********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("**********Confidentiality Protocol Link Results***********")
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

    # Click Terms of Use Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Terms-of-Use"

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
        print("****************Terms of Use Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Terms of Use Link Results*****************")
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

    # Click Disclaimers Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Disclaimers"

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
        print("****************Disclaimers Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Disclaimers Link Results******************")
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

    # Click Legal Notice Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Legal-Notice"

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
        print("****************Legal Notice Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Legal Notice Link Results*****************")
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

    # Click Privacy Policy Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(6) > a").click()
    expectedURL = StarrEnvironmentLink + "Privacy-Policy"

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
        print("***************Privacy Policy Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Privacy Policy Link Results****************")
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

    # Click Get in Touch Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.contact-us-cta.contact-us-cta--dark > div > div.contact-us-cta__button-wrapper > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])
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
        print("****************Get in Touch Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Get in Touch Link Results*****************")
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
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click Report a Claim Link
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(2)").click()
    expectedURL = StarrEnvironmentLink + "Client-Services/Claims"

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
        print("***************Report a Claim Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Report a Claim Link Results****************")
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

    # Reset Page
    driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()

    # Timestamp: Start Test
    testStart = datetime.now()

    # Click View All News Link
    driver.find_element(By.CSS_SELECTOR, "#content > div.newsfeed > div.newsfeed__view-all-container > div > a").click()
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
        print("***************View All News Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************View All News Link Results*****************")
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

    # Print Results Of Test Script
    print("##########################################")
    print("####### Footer Links Test Results ########")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

def test_starrInternationalLinks (testsPass, testsFail, testsWarning, testResult):
    print('....Checking International Links....')
    # Timestamp: Start Test
    testStart = datetime.now()

    # Open menu and click United Kingdom
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(1) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "https://starrcompanies.co.uk/"
    
    if newURL == expectedURL:
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
        print("***************United Kingdom Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************United Kingdom Link Results****************")
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
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open menu and click Brazil
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(2) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "https://www.starrcompanies.com.br/"
    
    if newURL == expectedURL:
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
        print("*******************Brazil Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Brazil Link Results********************")
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
    #                                     END TEST CASE #12                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open menu and click Chile
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(3) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "http://www.starrcompanies.cl/"
    
    if newURL == expectedURL:
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
        print("********************Chile Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Chile Link Results********************")
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
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open menu and click China
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(4) > a").click()
    driver.implicitly_wait(15)
    driver.switch_to.window(driver.window_handles[1])

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "http://www.starrchina.cn/"
    
    if newURL == expectedURL:
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
        print("********************China Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************China Link Results********************")
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
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open menu and click Japan
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(5) > a").click()

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "http://www.starrcompanies.jp/"
    
    if newURL == expectedURL:
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
        print("********************Japan Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Japan Link Results********************")
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

    # Go back
    driver.back()

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

    # Open menu and click Hong Kong
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(6) > a").click()

    # Split Google Analytics URL to validate
    newURL = driver.current_url.rsplit("?", 1)[0]
    expectedURL = "https://www.starrinsurance.com.hk/"
    
    if newURL == expectedURL:
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
        print("******************Hong Kong Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Hong Kong Link Results******************")
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

    # Go back
    driver.back()

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

    # Open menu and click Argentina
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(7) > a").click()
    expectedURL = StarrEnvironmentLink + "Country-Pages/Argentina"

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
        print("******************Argentina Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Argentina Link Results******************")
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

    # Go back
    driver.back()

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

    # Open menu and click Asia
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(8) > a").click()
    expectedURL = StarrEnvironmentLink + "Country-Pages/Asia"

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
        print("*********************Asia Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*********************Asia Link Results********************")
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

    # Go back
    driver.back()

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

    # Open menu and click Malta
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(9) > a").click()
    expectedURL = StarrEnvironmentLink + "Country-Pages/Malta"

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
        print("********************Malta Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Malta Link Results********************")
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

    # Go back
    driver.back()

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

    # Open menu and click Philippines
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(10) > a").click()
    expectedURL = StarrEnvironmentLink + "Country-Pages/Philippines"

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
        print("*****************Philippines Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Philippines Link Results*****************")
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

    # Go back
    driver.back()

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

    # Open menu and click Singapore
    driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(11) > a").click()
    expectedURL = StarrEnvironmentLink + "Country-Pages/Singapore"

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
        print("******************Singapore Link Results******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Singapore Link Results******************")
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

    # Go back
    driver.back()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #21                                    #
    ############################################################################################

    # Print Results Of Test Script
    print("##########################################")
    print("#### International Links Test Results ####")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

####################################################################################################
#                                        END FOOTER LINKS                                          #
####################################################################################################

test_starrHomePage (testsPass, testsFail, testsWarning, testResult)
test_starrFooterLinks (testsPass, testsFail, testsWarning, testResult)
test_starrInternationalLinks (testsPass, testsFail, testsWarning, testResult)
    #Test is complete

################################################################################################
################ Starr Companies Site Automation Footer Links Test Script ######################
################################################################################################