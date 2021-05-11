################################################################################################
##################### EXAMPLE SINGLE TEST CASE SCRIPT FOR TESTING PURPOSES #####################
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

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_domesticLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Domestic
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
 
        
        driver.switch_to.window(driver.window_handles[1])
        expectedURL = "https://www.starrlink.com/signin"

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > ui-view > div > div > div > div > div:nth-child(2) > div > div > div > div > div:nth-child(7) > button")))

        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Close Tab
        driver.close() 

        # Switch Back To First Tab
        driver.switch_to.window(driver.window_handles[0])

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