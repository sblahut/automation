################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################

import time
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFooterLinks(unittest.TestCase):
    
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
#                                      START HEADER LINKS                                          #
####################################################################################################

    ############################################################################################
    #                                    START TEST CASE #1                                    #
    ############################################################################################

    def test_logoLink (self):
        
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Logo Link
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.main-nav > a > img").click()
        expectedURL = StarrEnvironmentLink
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

    def test_careersLink (self):
        
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Careers Link
        driver.find_element(By.CSS_SELECTOR, "#header > header > div.sticky-nav > nav > div.sticky-nav__link > a").click()
        expectedURL = StarrEnvironmentLink + "Careers"
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

    def test_accidentAndHealthLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Accident and Health
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
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
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    def test_blanketAccidentLiabilityAndSpecialRisksLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Blanket Accident/Liability & Special Risks
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Blanket-Accident"
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

    def test_businessAccidentLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Business Accident
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Business-Accident"
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

    def test_groupAndIndividualADDLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Group & Individual AD&D
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Group-and-Individual-AD-and-D"
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

    def test_travelInsuranceLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Travel Insurance
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"
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

    def test_aviationAndAerospaceLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Aviation & Aerospace
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Aviation-and-Aerospace"
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

    def test_commercialGeneralCasualtyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Commercial General Casualty
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Commercial-General-Casualty"
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

    def test_constructionPrimaryAndExcessLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Construction Primary & Excess
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Construction-Primary-and-Excess"
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

    def test_contractorPollutionLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Contractor Pollution
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Contractor-Pollution"
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

    def test_crisisManagementLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Crisis Management
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Crisis-Management"
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

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################

    def test_cyberLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Cyber
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Cyber"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################

    def test_defenseBaseActLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Defense Base Act
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(6) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Defense-Base-Act"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################

    def test_energyPrimaryAndExcessCasualtyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Energy Primary & Excess Casualty
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(7) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Energy-Primary-and-Excess-Casualty"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #15                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #16                                    #
    ############################################################################################

    def test_environmentalLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Environmental
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(8) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Environmental"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #16                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #17                                    #
    ############################################################################################

    def test_federalEmployeeLiabilityLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Federal-Employee-Liability
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(9) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Federal-Employee-Liability"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #17                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #18                                    #
    ############################################################################################

    def test_financialLinesLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Financial Lines
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(10) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Finance"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #18                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #19                                    #
    ############################################################################################

    def test_politicalRiskLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Political Risk
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(11) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Political-Risk"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #19                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #20                                    #
    ############################################################################################

    def test_professionalLiabilityLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Professional Liability
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(12) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Professional-Liability"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #20                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #21                                    #
    ############################################################################################

    def test_riskManagementGeneralCasualtyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Risk Management General Casualty
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(13) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Risk-Management-General-Casualty"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #21                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #22                                    #
    ############################################################################################

    def test_sitePollutionLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Site Pollution
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(14) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Site-Pollution"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #22                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #23                                    #
    ############################################################################################

    def test_workersCompensationAndEmployerLiabilityLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Workers Compensation & Employer Liability
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(15) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Workers-Compensation-and-Employer-Liability"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #23                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #24                                    #
    ############################################################################################

    def test_inlandMarineLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Inland Marine
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #24                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #25                                    #
    ############################################################################################

    def test_marineLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Marine
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Marine/Marine"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #25                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #26                                    #
    ############################################################################################

    def test_generalPropertyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to General Property
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Property/General-Property"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #26                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #27                                    #
    ############################################################################################

    def test_energyTechnicalRisksLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Energy - Technical Risks
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Property/Energy---Technical-Risks"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #27                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #28                                    #
    ############################################################################################

    def test_constructionBuildersRiskLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Construction - Builders Risk
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Property/Construction---Builders-Risk"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #28                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #29                                    #
    ############################################################################################

    def test_propertyInlandMarineLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Inland Marine
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #29                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #30                                   #
    ############################################################################################

    def test_insuranceAviationAndAerospaceLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Aviation & Aerospace
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Aviation-and-Aerospace"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #30                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #31                                   #
    ############################################################################################

    def test_businessTravelLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Business Travel
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Business-Accident"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #31                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #32                                   #
    ############################################################################################

    def test_constructionLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Construction
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Construction"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #32                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #33                                   #
    ############################################################################################

    def test_energyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Energy
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Energy"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #33                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #34                                   #
    ############################################################################################

    def test_casualtyEnvironmentalLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Environmental
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(5) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Environmental"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #34                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #35                                   #
    ############################################################################################

    def test_foodAndBeverageLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Food & Beverage
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(6) > a").click()
        expectedURL = StarrEnvironmentLink + "Insurance/Food-and-Beverage"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #35                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #36                                   #
    ############################################################################################

    def test_governmentContractorsLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Government Contractors
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(7) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Defense-Base-Act"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #36                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #37                                   #
    ############################################################################################

    def test_hospitalityLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Hospitality
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(8) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Hospitality"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #37                                   #
    ############################################################################################
    
    ############################################################################################
    #                                    START TEST CASE #38                                   #
    ############################################################################################

    def test_manufacturingLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Manufacturing
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(9) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Manufacturing"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #38                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #39                                   #
    ############################################################################################

    def test_marineMarineLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Marine
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(10) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Marine/Marine"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #39                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #40                                   #
    ############################################################################################

    def test_realEstateLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Real Estate
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(11) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Real-Estate"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #40                                   #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #41                                   #
    ############################################################################################

    def test_retailLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Retail
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(12) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Retail"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #42                                   #
    ############################################################################################

    def test_travelLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Travel
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(2) > a").click()
        outOfViewLink = "#link-group-0 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(13) > a"
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element_by_css_selector(outOfViewLink))
        driver.find_element(By.CSS_SELECTOR, outOfViewLink).click()
        expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #42                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #43                                   #
    ############################################################################################

    def test_viewAllLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to View All
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > div > ul > li:nth-child(3) > a").click()  
        expectedURL = StarrEnvironmentLink + "Insurance/View-All"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #43                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #44                                   #
    ############################################################################################

    def test_starrAgentBrokerLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Become a Starr Agent/Broker
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(1) > a").click()  
        expectedURL = StarrEnvironmentLink + "Agents"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #44                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #45                                   #
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
        driver.implicitly_wait(300)
        driver.switch_to.window(driver.window_handles[1])
        expectedURL = "https://www.starrlink.com/signin"
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
    #                                      END TEST CASE #45                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #46                                   #
    ############################################################################################

    def test_internationalLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to International
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(2) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li.flyout-nav__list-item.flyout-nav__list-item--active > div > ul > li:nth-child(2) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])
        expectedURL = "https://international.starrlink.com/"
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
    #                                      END TEST CASE #46                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #47                                   #
    ############################################################################################


    def test_starrAssistLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Star Assist
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-1 > div > ul > li:nth-child(3) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])
        expectedURL = "https://travelagencies.starrassist.com/"
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
    #                                      END TEST CASE #47                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #48                                   #
    ############################################################################################

    def test_globalReachLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Global Offices
        driver.find_element(By.CSS_SELECTOR, "#link-group-2 > a").click()
        expectedURL = StarrEnvironmentLink + "Global-Reach"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #48                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #49                                   #
    ############################################################################################

    def test_whoWeAreLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Who We Are
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(1) > a").click()
        expectedURL = StarrEnvironmentLink + "About/Who-We-Are"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #49                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #50                                   #
    ############################################################################################

    def test_historyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to History
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "About/History"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #50                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #51                                   #
    ############################################################################################

    def test_leadershipLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Leadership
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "About/Leadership"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #51                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #52                                   #
    ############################################################################################

    def test_investmentsLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Leadership
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "About/Investments"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #52                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #53                                   #
    ############################################################################################

    def test_clientServicesLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Client Services
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-3 > div > ul > li:nth-child(5) > a").click()
        expectedURL = StarrEnvironmentLink + "Client-Services"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #53                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #54                                   #
    ############################################################################################

    def test_contactUsLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to Contact Us
        driver.find_element(By.CSS_SELECTOR, "#link-group-4 > a").click()
        expectedURL = StarrEnvironmentLink + "Contact-Us"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #54                                   #
    ############################################################################################

    ############################################################################################
    #                                      END TEST CASE #55                                   #
    ############################################################################################

    def test_newsLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open Nav and navigate to News
        driver.find_element(By.CSS_SELECTOR, "#link-group-5 > a").click()
        expectedURL = StarrEnvironmentLink + "News"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                      END TEST CASE #55                                   #
    ############################################################################################
    
####################################################################################################
#                                        END HEADER LINKS                                          #
####################################################################################################

    #Test is complete

################################################################################################
################ Starr Companies Site Automation Header Links Test Script ######################
################################################################################################

if __name__ == '__main__':
    unittest.main()