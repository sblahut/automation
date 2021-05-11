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

        #driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__search-container > form > label > svg").click()

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
    #                                     END TEST CASE #1                                     #
    ############################################################################################

if __name__ == '__main__':
    unittest.main()

################################################################################################
##################### EXAMPLE SINGLE TEST CASE SCRIPT FOR TESTING PURPOSES #####################
################################################################################################