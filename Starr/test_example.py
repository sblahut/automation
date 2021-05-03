################################################################################################
################# Starr Companies Site Automation Search Component Test Script #################
################################################################################################

import time
import requests
import unittest
from pynput.keyboard import Key, Controller
from itertools import islice
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchComponent(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')
        
        # Open Domain
        self.driver.get("https://www.starrcompanies.com/")
        # Accept Cookies
        self.driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click() 
    
    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_starrHomePage (self):
         
        # Loading message
        print("....Checking Starr Companies homepage....")

        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedHomePageLoadTimeInSeconds = 20

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        expectedURL = StarrEnvironmentLink
        
        self.assertEqual(driver.current_url, expectedURL)
            
        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)
        
        self.assertGreaterEqual (expectedHomePageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))  

####################################################################################################
#                                      START SEARCH COMPONENT                                      #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_searchTestCaseOne (self):
        
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('TRAVEL')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()
        


        expectedURL = StarrEnvironmentLink + "search?term=TRAVEL"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        ids = driver.find_elements_by_class_name('search-results__result-title')

        for id in islice(ids, 0, 1, 1):

            result = (str(id.text))
            
            word = 'travel'

            contains_word = word in result.lower()
            
            self.assertFalse(contains_word, "ALERT: Search is not functioning as expected!")

        # Wait
        driver.implicitly_wait(15)
    ############################################################################################
    #                                     END TEST CASE #1                                     #
    ############################################################################################

if __name__ == '__main__':
    unittest.main()