################################################################################################
#################### Geekhive Site Automation Contact Form Test Script #########################
################################################################################################
import pytest
import time
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC

# Main Domain Link
GeekhiveEnvironmentLink = "https://www.geekhive.com/"

# Expected Page Load Time
expectedPageLoadTimeInSeconds = 3

# Declaration of Wait Time

# Results Declaration
TestsPass = 0
TestsFail = 0
TestsWarning = 0
testResult = ""

# Record Script Start Time for Script Duration
scriptStart = datetime.now()

# Declare Chrome Driver
driver = webdriver.Chrome("./chromedriver")

# Wait
driver.implicitly_wait(15)

# Loading message
print("....Navigating to the Geekhive webpage...")

# Open Geekhive Site
driver.get("https://www.geekhive.com/")

# Set Window Size
driver.set_window_size(1400, 1214)

####################################################################################################
#                                      START CONTACT FORM                                          #
####################################################################################################
 
# Open Contact Page
driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(8) > .btn").click()

# Enter 'Steven' in First Name Field
driver.find_element(By.ID, "edit-first-name").click()
driver.find_element(By.ID, "edit-first-name").send_keys("Steven")

# Wait 1 Second
time.sleep(1)

# Enter 'Test' in Last Name Field
driver.find_element(By.ID, "edit-last-name").send_keys("Test")
driver.find_element(By.ID, "edit-email").send_keys("sblahut@geekhive.com")

# Wait 2 Seconds
time.sleep(2)

# Enter 'Test Message' in Message Field
driver.find_element(By.ID, "edit-description").send_keys("Test Message")

# Wait 2 Seconds
time.sleep(2)

            ######################### Start Recaptcha Work #########################  

# Wait 1 Second
time.sleep(1)

# Click on reCAPTCHA Box
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

time.sleep(3)

##########################
## POP-UP FOR RECAPTCHA ##
##########################

#WebDriverWait(self.driver, css=.recaptcha-checkbox-border).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border")))
#driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()

# Submit Form
driver.find_element(By.ID, "edit-actions-submit").click()

            ########################## End Recaptcha Work ##########################  


####################################################################################################
#                                       END CONTACT FORM                                           #
####################################################################################################
  
