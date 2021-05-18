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
    #                                     END TEST CASE #1                                     #
    ############################################################################################

if __name__ == '__main__':
    unittest.main()

################################################################################################
##################### EXAMPLE SINGLE TEST CASE SCRIPT FOR TESTING PURPOSES #####################
################################################################################################