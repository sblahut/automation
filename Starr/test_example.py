################################################################################################
################ Starr Companies Site Automation Hamburger Links Test Script ###################
################################################################################################

import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHamburgerNavLinks(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_argument('disable-infobars')
        self.driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')
        
        # Open Domain
        self.driver.get("https://www.starrcompanies.com/")
        # Accept Cookies
        self.driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click() 
        self.driver.set_window_size(664, 620)
        
    # tearDown runs after each test case
    def tearDown(self):
        self.driver.quit()

    def test_starrHomePage (self):

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
#                                     START HAMBURGER LINKS                                        #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_accidentAndHealthLink (self):
        
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Accident and Health 
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Accident-and-Health"
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

if __name__ == '__main__':
    unittest.main()