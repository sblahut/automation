################################################################################################
################ Starr Companies Site Automation Footer Links Test Script ######################
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
#                                      START FOOTER LINKS                                          #
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
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__logo > a > img").click()
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
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(1) > a").click()
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

    def test_complianceAndEthicsLink (self):
        print('....Checking Footer Links....')    
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Compliance and Ethics Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(2) > a").click()
        expectedURL = StarrEnvironmentLink + "Compliance-and-Ethics"
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

    def test_termsOfUseLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Terms of Use Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(3) > a").click()
        expectedURL = StarrEnvironmentLink + "Terms-of-Use"
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

    def test_disclaimersLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Disclaimers Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(4) > a").click()
        expectedURL = StarrEnvironmentLink + "Disclaimers"
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

    def test_legalNoticeLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Legal Notice Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(5) > a").click()
        expectedURL = StarrEnvironmentLink + "Legal-Notice"
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

    def test_privacyPolicyLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Privacy Policy Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__links > div:nth-child(6) > a").click()
        expectedURL = StarrEnvironmentLink + "Privacy-Policy"
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

    def test_getInTouchLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Get in Touch Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.contact-us-cta.contact-us-cta--dark > div > div.contact-us-cta__button-wrapper > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])
        expectedURL = StarrEnvironmentLink + "Contact-Us"
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
    #                                      END TEST CASE #8                                    #
    ############################################################################################

    ############################################################################################
    #                                    START TEST CASE #9                                    #
    ############################################################################################

    def test_claimLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click Report a Claim Link
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(2)").click()
        expectedURL = StarrEnvironmentLink + "Client-Services/Claims"
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

    def test_viewAllNewsLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Click View All News Link
        driver.find_element(By.CSS_SELECTOR, "#content > div.newsfeed > div.newsfeed__view-all-container > div > a").click()
        expectedURL = StarrEnvironmentLink + "News"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Wait
        driver.implicitly_wait(15)
        print('....Footer Links Complete....')
    ############################################################################################
    #                                     END TEST CASE #10                                    #
    ############################################################################################
    
    
    ############################################################################################
    #                                   START TEST CASE #11                                    #
    ############################################################################################

    def test_unitedKingdomLink (self):
        print('....Checking International Links....')
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click United Kingdom
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(1) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "https://starrcompanies.co.uk/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #11                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #12                                    #
    ############################################################################################
    
    def test_brazilLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Brazil
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(2) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "https://www.starrcompanies.com.br/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #12                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #13                                    #
    ############################################################################################
    
    def test_chileLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Chile
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(3) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "http://www.starrcompanies.cl/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #13                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #14                                    #
    ############################################################################################
    
    def test_chinaLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click China
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(4) > a").click()
        driver.implicitly_wait(15)
        driver.switch_to.window(driver.window_handles[1])

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "https://www.starrchina.cn/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #14                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #15                                    #
    ############################################################################################
    
    def test_japanLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Japan
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(5) > a").click()

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "http://www.starrcompanies.jp/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #15                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #16                                    #
    ############################################################################################

    def test_hongkongLink (self):
            
        driver = self.driver
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Hong Kong
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(6) > a").click()

        # Split Google Analytics URL to validate
        newURL = driver.current_url.rsplit("?", 1)[0]
        expectedURL = "https://www.starrinsurance.com.hk/"
        self.assertEqual(newURL, expectedURL)

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
    #                                     END TEST CASE #16                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #17                                    #
    ############################################################################################

    def test_argentinaLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Argentina
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(7) > a").click()
        expectedURL = StarrEnvironmentLink + "Country-Pages/Argentina"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Go back
        driver.back()

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #17                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #18                                    #
    ############################################################################################

    def test_asiaLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Asia
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(8) > a").click()
        expectedURL = StarrEnvironmentLink + "Country-Pages/Asia"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Go back
        driver.back()

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #18                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #19                                    #
    ############################################################################################

    def test_maltaLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Malta
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(9) > a").click()
        expectedURL = StarrEnvironmentLink + "Country-Pages/Malta"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Go back
        driver.back()

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #19                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #20                                    #
    ############################################################################################

    def test_philippinesLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Philippines
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(10) > a").click()
        expectedURL = StarrEnvironmentLink + "Country-Pages/Philippines"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Go back
        driver.back()

        # Wait
        driver.implicitly_wait(15)

    ############################################################################################
    #                                     END TEST CASE #20                                    #
    ############################################################################################

    ############################################################################################
    #                                   START TEST CASE #21                                    #
    ############################################################################################

    def test_singaporeLink (self):
            
        driver = self.driver
        StarrEnvironmentLink = "https://www.starrcompanies.com/"
        expectedPageLoadTimeInSeconds = 10

        # Wait
        driver.implicitly_wait(15)

        # Timestamp: Start Test
        testStart = datetime.now()

        # Open menu and click Singapore
        driver.find_element(By.CSS_SELECTOR, "#footer > footer > div.footer__buttons > a:nth-child(1)").click()
        driver.find_element(By.CSS_SELECTOR, "#FooterCountries > div:nth-child(11) > a").click()
        expectedURL = StarrEnvironmentLink + "Country-Pages/Singapore"
        self.assertEqual(driver.current_url, expectedURL)

        # Timestamp: End Test
        testEnd = datetime.now()

        # Record Results
        testTime = (testEnd - testStart)

        self.assertGreaterEqual (expectedPageLoadTimeInSeconds, testTime.seconds, "Page load time is slow. Time: " + str(testTime))

        # Go back
        driver.back()

        # Wait
        driver.implicitly_wait(15)
        print('....International Links Complete....') 
    ############################################################################################
    #                                     END TEST CASE #21                                    #
    ############################################################################################
     
####################################################################################################
#                                        END FOOTER LINKS                                          #
####################################################################################################

    #Test is complete

################################################################################################
################ Starr Companies Site Automation Footer Links Test Script ######################
################################################################################################

if __name__ == '__main__':
    unittest.main()