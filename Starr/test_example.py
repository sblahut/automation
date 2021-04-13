################################################################################################
################# Starr Companies Site Automation Search Component Test Script #################
################################################################################################

import time
import requests
import unittest
from pynput.keyboard import Key, Controller
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearch(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_starrHomePage (self):

        driver = self.driver

        # Expected Page Load Time
        expectedPageLoadTimeInSeconds = 20

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Loading message
        print("....Navigating to the Starr Companies homepage...")

        # Main Domain Link
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
            
        # Open Domain
        driver.get("https://www.starrcompanies.com/")

        expectedURL = StarrEnvironmentLink
        
        self.assertEqual(driver.current_url, expectedURL)
            
        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        
        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

####################################################################################################
#                                      START SEARCH COMPONENT                                      #
####################################################################################################
    
    # Accept Cookies
    #driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click()

####################################################################################################
#                                       END SEARCH COMPONENT                                       #
####################################################################################################

#test_starrHomePage (testsPass,testsFail, testsWarning, testResult)

if __name__ == '__main__':
    unittest.main()