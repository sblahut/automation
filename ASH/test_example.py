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
        #self.driver.set_window_size(800,600)
        
    # Teardown
    def tearDown(self):
        self.driver.quit()

    def test_ashStoreLink (self):
        
        driver = self.driver
        expectedPageLoadTimeInSeconds = 3

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Global Initiatives Link
        driver.find_element(By.CSS_SELECTOR, ".nav-toggle").click()
        driver.set_window_size(1200,800)
        driver.implicitly_wait(15)
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        driver.find_element(By.CSS_SELECTOR, "#navbarCollapse > div > div.side-menu-container__white-section > ul > li:nth-child(6) > a").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#navbar > a > img.logo")))
        tag = "store"
        self.assertIn(tag, driver.current_url)

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