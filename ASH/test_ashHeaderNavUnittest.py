################################################################################################
######### American Society of Hematology Site Automation Header Links Test Script ##############
################################################################################################

import unittest
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

class TestHeaderLinks(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')
        
        # Open Domain
        self.driver.get("https://www.hematology.org/")

    # Teardown
    def tearDown(self):
        self.driver.quit()

    def test_ashHomePage (self):
    
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Ash Site
        #driver.get("https://www.hematology.org/") // Open from setUp method.
        expectedURL = AshEnvironmentLink
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))  

####################################################################################################
#                                      START HEADER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_logoLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Logo Link
        driver.find_element(By.CSS_SELECTOR, ".logo").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #1                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    def test_researchLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Research Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(1) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "research"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #2                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    def test_educationLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Education Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(2) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "education"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    def test_advocacyLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Advocacy Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(3) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "advocacy"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #4                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    def test_careersLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Careers Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(4) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "about/careers"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #5                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

    def test_meetingsLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Meetings Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(5) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "meetings"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #6                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #7                                    #
    ############################################################################################

    def test_publicationsLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Publications Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(6) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "publications"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #7                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #8                                    #
    ############################################################################################

    def test_awardsLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Awards Link
        driver.find_element(By.CSS_SELECTOR, ".justify-content-between > .nav-item:nth-child(7) > .nav-link").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "awards"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    def test_newsroomLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Newsroom Link
        driver.find_element(By.CSS_SELECTOR, "#navbar > div > ul > li:nth-child(8) > a").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "newsroom"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #9                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #10                                    #
    ############################################################################################

    def test_aboutAshLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click About Ash Link
        driver.find_element(By.CSS_SELECTOR, "#top-nav > li:nth-child(1) > a").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "about"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #10                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

    def test_ashFoundationLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Ash Foundation Link
        driver.find_element(By.CSS_SELECTOR, "#top-nav > li:nth-child(2) > a").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "foundation"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################

    def test_logInLink (self):
        
        driver = self.driver
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Log In Link
        driver.find_element(By.CSS_SELECTOR, ".my-account__button-text").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#okta-sign-in > div.okta-sign-in-header.auth-header > img")))
        expectedURL = "https://sso.hematology.org/"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #12                                    #
    ############################################################################################

####################################################################################################
#                                        END HEADER LINKS                                          #
####################################################################################################

#Test is complete
if __name__ == '__main__':
    unittest.main()

################################################################################################
######### American Society of Hematology Site Automation Header Links Test Script ##############
################################################################################################