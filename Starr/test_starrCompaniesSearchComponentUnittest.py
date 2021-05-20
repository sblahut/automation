################################################################################################
################# Starr Companies Site Automation Search Component Test Script #################
################################################################################################

import time
import unittest
from pynput.keyboard import Key, Controller
from itertools import islice
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchComponent(unittest.TestCase):
    
    def setUp(self):
        # Declare Chrome Driver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        
        # Open Domain
        self.driver.get("https://www.starrcompanies.com/")
        # Accept Cookies
        self.driver.find_element(By.CSS_SELECTOR, "body > div.privacy-warning.permisive > div.submit > a").click() 
    
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
#                                      START SEARCH COMPONENT                                      #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_searchTestCaseOne (self):
        
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('TRAVEL')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()
        
        expectedURL = StarrEnvironmentLink + "search?term=TRAVEL"
        self.assertEqual(driver.current_url, expectedURL)

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #1                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    def test_searchTestCaseTwo (self):

        driver = self.driver

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('TRAVEL')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()
        
        ids = driver.find_elements_by_class_name('search-results__result-title')

        for id in islice(ids, 0, 1, 1):

            result = (str(id.text))           
            word = 'travel'       
            contains_word = word in result.lower()
            self.assertTrue(contains_word, "ALERT: Search is not functioning as expected!")

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #2                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    def test_searchTestCaseThree (self):
    
        driver = self.driver

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('TRAVEL')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()
        
        # Switch to coverages
        driver.find_element(By.CSS_SELECTOR, "#content > div.search-results > div > div.search-results__rightrail > a:nth-child(3)").click()

        # Added wait to ensure results are updated
        time.sleep(2)

        # Run results
        ids = driver.find_elements_by_class_name('search-results__result-title')

        for id in islice(ids, 0, 1, 1):
        
            result = (str(id.text)) 
            word = 'travel'
            word2 = 'insurance'
            contains_words = word and word2 in result.lower()
            self.assertTrue(contains_words, "ALERT: Search is not functioning as expected!")

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #3                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    def test_searchTestCaseFour (self):
        
        driver = self.driver

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('GEEKHIVE')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

        # Run results
        ids = driver.find_elements_by_class_name('search-results__no-results-text')

        for id in islice(ids, 0, 1, 1):

            result = (str(id.text))
            self.assertEqual(result, "No Results", "ALERT: Search is not functioning as expected!")

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #4                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    def test_searchTestCaseFive (self):
        
        driver = self.driver

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('STARR INVESTMENT HOLDINGS')
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

        # Run results
        ids = driver.find_elements_by_class_name('search-results__result-title')

        for id in islice(ids, 0, 1, 1):

            result = (str(id.text))
            word = 'starr investment holdings'
            contains_word = word in result.lower()
            self.assertTrue(contains_word, "ALERT: Search is not functioning as expected!")
    
        # Wait
        driver.implicitly_wait(15)
        
    ############################################################################################
    #                                     END TEST CASE #5                                     #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

    def test_searchTestCaseSeven (self):

        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        print('....Testing the ability to search for special charaters without redirect or crash....')

        # Open search
        driver.find_element(By.CSS_SELECTOR, "#search-toggle > svg").click()
        search = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > input")))
        search.send_keys('!@#$%^')

        # Pressing and releasing enter from the search box
        print('....Testing the ability to hit enter from after typing...')
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(2)

        expectedURL = StarrEnvironmentLink + "search?term=%21%40%23%24%25%5E"
        self.assertEqual(driver.current_url, expectedURL)

        # Run results
        ids = driver.find_elements_by_class_name('search-results__no-results-text')

        for id in islice(ids, 0, 1, 1):
        
            result = (str(id.text))
            self.assertEqual(result, "No Results", "ALERT: Search is not functioning as expected!")
    
        # Wait
        driver.implicitly_wait(15)
        
    ############################################################################################
    #                                     END TEST CASE #6                                     #
    ############################################################################################
    
####################################################################################################
#                                       END SEARCH COMPONENT                                       #
####################################################################################################

#Test is complete
if __name__ == '__main__':
    unittest.main()

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################