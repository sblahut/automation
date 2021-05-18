################################################################################################
######### American Society of Hematology Site Automation Footer Links Test Script ##############
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

class TestFooterLinks(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')
        
        # Open Domain
        self.driver.get("https://www.hematology.org/")
        #Scroll Down To Footer
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 9999)")

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
#                                      START FOOTER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_facebookLink (self):
        
        driver = self.driver
        expectedExternalPageLoadTimeInSeconds = 5

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Facebook Link
        driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(1)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#blueBarDOMInspector > div > div > div > div.lfloat._ohe > a > i")))
        expectedURL = "https://www.facebook.com/AmericanSocietyofHematology"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedExternalPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

        # Go back to the previous page
        driver.back()

    ############################################################################################
    #                                      END TEST CASE #1                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    def test_linkedInLink (self):
        
        driver = self.driver
        expectedExternalPageLoadTimeInSeconds = 5

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click LinkedIn Link
        driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(2)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > img")))
        tag = "linkedin"
        self.assertIn(tag, driver.current_url)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedExternalPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

        # Go back to the previous page
        driver.back()

    ############################################################################################
    #                                      END TEST CASE #2                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    def test_twitterLink (self):
        
        driver = self.driver
        expectedExternalPageLoadTimeInSeconds = 5

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Twitter Link
        driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(3)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div > div.css-1dbjc4n.r-dnmrzs.r-1vvnge1 > h1 > a > div > svg > g > path")))
        expectedURL = "https://twitter.com/ASH_hematology"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedExternalPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

        # Go back to the previous page
        driver.back()

    ############################################################################################
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    def test_youTubeLink (self):
        
        driver = self.driver
        expectedExternalPageLoadTimeInSeconds = 5

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click YouTube Link
        driver.find_element(By.CSS_SELECTOR, ".footer__social-button:nth-child(4)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#logo-icon")))
        expectedURL = "https://www.youtube.com/user/ASHWebmaster"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        self.assertGreaterEqual (expectedExternalPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

        # Go back to the previous page
        driver.back()

    ############################################################################################
    #                                      END TEST CASE #4                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    def test_supportOpportunitiesLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Support Opportunities Link
        driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(1)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "about/corporate-support"
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

    def test_privacyPoliciesLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Privacy Policy Link
        driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(2)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "about/privacy-policy"
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

    def test_termsOfServiceLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Terms of Service Link
        driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(3)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "about/terms-of-service"
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

    def test_contactUsLink (self):
        
        driver = self.driver
        AshEnvironmentLink = "https://www.hematology.org/"
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Contact Us Link
        driver.find_element(By.CSS_SELECTOR, "body > footer > div.footer-bar.d-flex > p:nth-child(3) > a:nth-child(4)").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        expectedURL = AshEnvironmentLink + "contact-us"
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

####################################################################################################
#                                        END FOOTER LINKS                                          #
####################################################################################################

#Test is complete
if __name__ == '__main__':
    unittest.main()

################################################################################################
######### American Society of Hematology Site Automation Footer Links Test Script ##############
################################################################################################