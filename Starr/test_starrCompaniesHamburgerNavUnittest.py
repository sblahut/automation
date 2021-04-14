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

    ############################################################################################
    #                                    START TEST CASE #2                                    #
    ############################################################################################

    def test_blanketAccidentLiabilityAndSpecialRisksLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Blanket Accident/Liability & Special Risks
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > div > ul > li:nth-child(2) > a").click()
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
    #                                      END TEST CASE #2                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #3                                    #
    ############################################################################################

    def test_businessAccidentLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Business Accident
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > div > ul > li:nth-child(3) > a").click()
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
    #                                      END TEST CASE #3                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #4                                    #
    ############################################################################################

    def test_groupAndIndividualADDLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Group & Individual AD&D
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > div > ul > li:nth-child(4) > a").click()
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
    #                                      END TEST CASE #4                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #5                                    #
    ############################################################################################

    def test_travelInsuranceLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Travel Insurance
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > div > ul > li:nth-child(5) > a").click()
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
    #                                      END TEST CASE #5                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #6                                    #
    ############################################################################################

    def test_aviationAndAerospaceLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Aviation & Aerospace
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(2) > div > ul > li > a").click()
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
    #                                      END TEST CASE #6                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #7                                    #
    ############################################################################################

    def test_commercialGeneralCasualtyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Commercial General Casualty
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(1) > a").click()
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
    #                                      END TEST CASE #7                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #8                                    #
    ############################################################################################

    def test_constructionPrimaryAndExcessLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Construction Primary & Excess
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(2) > a").click()
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
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    def test_contractorPollutionLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Contractor Pollution
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(3) > a").click()
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
    #                                      END TEST CASE #9                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #10                                    #
    ############################################################################################

    def test_crisisManagementLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Crisis Management
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(4) > a").click()
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
    #                                     END TEST CASE #10                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

    def test_cyberLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Cyber
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(5) > a").click()
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
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################

    def test_defenseBaseActLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Defense Base Act
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(6) > a").click()
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
    #                                     END TEST CASE #12                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################

    def test_energyPrimaryAndExcessCasualtyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Energy Primary & Excess Casualty
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(7) > a").click()
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
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################

    def test_environmentalLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Environmental
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(8) > a").click()
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
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################

    def test_federalEmployeeLiabilityLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open hamburger menu and select Federal Employee Liability
        driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
        driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
        driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(9) > a").click()
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
    #                                     END TEST CASE #15                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #16                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Financial Lines
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(10) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Finance"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Financial Lines Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Financial Lines Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #16                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #17                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Political Risk
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(11) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Political-Risk"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Political Risk Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Political Risk Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #17                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #18                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Professional Liability
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(12) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Professional-Liability"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("************Professional Liability Link Results************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Professional Liability Link Results************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #18                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #19                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Risk Management General Casualty
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(13) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Risk-Management-General-Casualty"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******Risk Management General Casualty Link Results*******")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******Risk Management General Casualty Link Results*******")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #19                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #20                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Site Pollution
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(14) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Site-Pollution"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Site Pollution Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Site Pollution Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #20                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #21                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Worker's Compensation & Employer Liability
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > div > ul > li:nth-child(15) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Workers-Compensation-and-Employer-Liability"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("************Worker's Compensation Link Results************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Worker's Compensation Link Results************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #21                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #22                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Inland Marine
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(4) > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Inland Marine Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Inland Marine Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #22                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #23                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Marine
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(4) > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Marine"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("********************Marine Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Marine Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #23                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #24                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select General Property
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(5) > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/General-Property"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************General Property Link Results**************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************General Property Link Results**************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #24                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #25                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Energy - Technical Risks
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(5) > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Energy---Technical-Risks"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***********Energy - Technical Risks Link Results**********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***********Energy - Technical Risks Link Results**********")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #25                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #26                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Construction - Builders Risk
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(5) > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Construction---Builders-Risk"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*********Construction - Builders Risk Link Results********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*********Construction - Builders Risk Link Results********")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #26                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #27                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Inland Marine
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(5) > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Property/Inland-Marine"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Inland Marine Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Inland Marine Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #27                                    #
    ############################################################################################

    # Print Results Of Test Script
    print("##########################################")
    print("###### Products Links Test Results #######")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                   START TEST CASE #28                                    #
    ############################################################################################

def test_starrIndustryLinks (testsPass, testsFail, testsWarning, testResult):
    print('....Checking Industry Links....')
    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Aviation & Aerospace
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Aviation-and-Aerospace"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("************Aviation & Aerospace Link Results*************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Aviation & Aerospace Link Results*************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #28                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #29                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Business Travel
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Business-Accident"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Business Travel Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Business Travel Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #29                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #30                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Construction
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Construction"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Construction Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Construction Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #30                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #31                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Energy
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Energy"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************Energy Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Energy Link Results********************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #31                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #32                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Environmental
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Environmental"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Environmental Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Environmental Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #32                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #33                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Food & Beverage
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(6) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Food-and-Beverage"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Food & Beverage Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Food & Beverage Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #33                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #34                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Government Contractors
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(7) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Casualty/Defense-Base-Act"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("************Government Contractors Link Results***********")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("************Government Contractors Link Results***********")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #34                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #35                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Hospitality
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(8) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Hospitality"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*****************Hospitality Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Hospitality Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #35                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #36                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Manufacturing
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(9) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Manufacturing"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Manufacturing Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Manufacturing Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #36                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #37                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Marine
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(10) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Marine/Marine"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("********************Marine Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************Marine Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #37                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #38                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Real Estate
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(11) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Real-Estate"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*****************Real Estate Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Real Estate Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #38                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #39                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Retail
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(12) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Retail"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************Retail Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Retail Link Results********************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #39                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #40                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Travel
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(13) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/Accident/Travel-Insurance"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************Travel Link Results********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Travel Link Results********************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #40                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #41                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select View All
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-0 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "Insurance/View-All"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******************View All Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************View All Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #41                                    #
    ############################################################################################

    # Print Results Of Test Script
    print("##########################################")
    print("###### Industry Links Test Results #######")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

    ############################################################################################
    #                                   START TEST CASE #42                                    #
    ############################################################################################


def test_starrRemainderLinks (testsPass, testsFail, testsWarning, testResult):
    print('....Checking Remainder Links....')
    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Become a Starr Agent/Broker
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "Agents"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Become a Starr Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Become a Starr Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #42                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #43                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Domestic
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(1) > a").click()
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://www.starrlink.com/"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******************Domestic Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Domestic Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Close Tab
    driver.close()

    # Switch Back To First Tab
    driver.switch_to.window(driver.window_handles[0])

    # Close menu
    driver.find_element(By.CSS_SELECTOR, "#close-menu > svg").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #43                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #44                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select International
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--tertiary > div > div > ul > li:nth-child(2) > a").click()
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://international.starrlink.com/"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************International Link Results****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************International Link Results****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Close Tab
    driver.close()

    # Switch Back To First Tab
    driver.switch_to.window(driver.window_handles[0])

    # Close menu
    driver.find_element(By.CSS_SELECTOR, "#close-menu > svg").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #44                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #45                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select StarrAssist
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-1 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(3) > a").click()
    driver.switch_to.window(driver.window_handles[1])
    expectedURL = "https://travelagencies.starrassist.com/"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*****************StarrAssist Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************StarrAssist Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Close Tab
    driver.close()

    # Switch Back To First Tab
    driver.switch_to.window(driver.window_handles[0])

    # Close menu
    driver.find_element(By.CSS_SELECTOR, "#close-menu > svg").click()

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #45                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #46                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Global Offices
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-2 > a").click()
    expectedURL = StarrEnvironmentLink + "Global-Reach"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("****************Global Offices Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("****************Global Offices Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #46                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #47                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Who We Are
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(1) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Who-We-Are"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******************Who We Are Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Who We Are Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #47                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #48                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select History
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(2) > a").click()
    expectedURL = StarrEnvironmentLink + "About/History"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************History Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************History Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #48                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #49                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Leadership
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(3) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Leadership"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******************Leadership Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Leadership Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #49                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #50                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Investments
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(4) > a").click()
    expectedURL = StarrEnvironmentLink + "About/Investments"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*****************Investments Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*****************Investments Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #50                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #51                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Client Services
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-3 > a").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > section > nav.flyout-nav.flyout-nav--secondary > div > div > ul > li:nth-child(5) > a").click()
    expectedURL = StarrEnvironmentLink + "Client-Services"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("***************Client Services Link Results***************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("***************Client Services Link Results***************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #51                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #52                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Contact Us
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-4 > a").click()
    expectedURL = StarrEnvironmentLink + "Contact-Us"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("******************Contact Us Link Results*****************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("******************Contact Us Link Results*****************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #52                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #53                                    #
    ############################################################################################

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select News
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#link-group-5 > a").click()
    expectedURL = StarrEnvironmentLink + "News"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("********************News Link Results*********************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("********************News Link Results*********************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #53                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #54                                    #
    ############################################################################################
        
    # Set Window Size
    driver.set_window_size(620, 750)

    # Timestamp: Start Test
    testStart = datetime.now()

    # Open hamburger menu and select Careers
    driver.find_element(By.CSS_SELECTOR, "#hamburger_icon").click()
    driver.find_element(By.CSS_SELECTOR, "#header > header > section > footer > a").click()
    expectedURL = StarrEnvironmentLink + "Careers"

    if driver.current_url == expectedURL:
        testResult = "Pass"
    else:
        testResult = "Fail"

    # Timestamp: End Test
    testEnd = datetime.now()

    # Validation of Page Load Speed
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        speedTestResult = "Warning"
        testNotes = "Page load time is slow. Time: " + str(testTime)
    else:
        speedTestResult = "Pass"
        testNotes = "Page load time is: " + str(testTime)

    # Record Results
    testTime = (testEnd - testStart)

    if testResult == "Fail":
        print("*******************Careers Link Results*******************")
        print("URL Test Result: " + str(testResult))
        print("**********************************************************")

    if speedTestResult == "Warning":
        print("*******************Careers Link Results*******************")
        print("Speed Test Result: " + str(speedTestResult))
        print(testNotes)
        print("**********************************************************")

    # Record Results To Tally For Final Results
    if testResult == "Pass":
        testsPass += 1
    elif testResult == "Fail":
        testsFail += 1
    elif testResult == "Warning":
        testsWarning += 1

    if speedTestResult == "Pass":
        testsPass += 1
    elif speedTestResult == "Fail":
        testsFail += 1
    elif speedTestResult == "Warning":
        testsWarning += 1

    # Wait
    driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #54                                    #
    ############################################################################################

    # Print Results Of Test Script
    print("##########################################")
    print("###### Remainder Links Test Results ######")
    print("##########################################")
    print("Number of Pass Results: " + str(testsPass))
    print("Number of Fail Results: " + str(testsFail))
    print("Number of Warnings: " + str(testsWarning))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")

####################################################################################################
#                                       END HAMBURGER LINKS                                        #
####################################################################################################

test_starrHomePage (testsPass, testsFail, testsWarning, testResult)
test_starrProductLinks (testsPass, testsFail, testsWarning, testResult)
test_starrIndustryLinks (testsPass, testsFail, testsWarning, testResult)
test_starrRemainderLinks (testsPass, testsFail, testsWarning, testResult)
    #Test is complete

################################################################################################
################ Starr Companies Site Automation Hamburger Links Test Script ###################
################################################################################################