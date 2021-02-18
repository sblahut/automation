################################################################################################
############### World Courier Site Automation Incident Calculator Test Script ##################
################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from itertools import islice
from bs4 import BeautifulSoup
import os
import datetime
import requests

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.datetime.now()

print("                                          ")
print('....Navigating to World Courier Incident Calculator Page....')
print("                                          ")

# Open world courier website
driver.get('https://www.worldcourier.com/incident-calculator/')
# Accept Cookies
#driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

def test_abcWorldCourierIncidentCalculator ():

    print('....Filling out calculator....')
    print("                                          ")
    # Number of associates
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aA1"))).send_keys('5') 
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aA2"))).send_keys('5')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aA3"))).send_keys('5')

    # Hours per excursion per associate
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aB1"))).send_keys('5')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aB2"))).send_keys('5')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aB3"))).send_keys('5')

    # Hourly rate
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aD1"))).send_keys('5')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aD2"))).send_keys('5')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#aD3"))).send_keys('5')

    # Cost of goods
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bA1"))).send_keys('5')

    # Units per shipping box
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bB1"))).send_keys('5')

    # Shipping
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bD1"))).send_keys('5')

    # Destruction
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bE1"))).send_keys('5')

    print('....Calculating my results....')
    print("                                          ")
    # Calculate my results
    calculate = driver.find_element(By.CSS_SELECTOR, "#calculate")
    driver.execute_script("arguments[0].click();", calculate)
    
    # Run results
    ids = driver.find_elements(By.CSS_SELECTOR, "#resultContainer > div.background-white > div > div:nth-child(2) > div > div")

    for id in ids:
        print("                                          ")
        print("##########################################")
        print("######## Test Case #1: Calculate #########")
        print(id.text)
        print("##########################################")
        print("                                          ")
    
def test_abcWorldCourierSubmitForm ():

    print('....Filling out form....')
    print("                                          ")
    # First Name
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40first_name"))).send_keys('Test')
    
    # Last name
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40last_name"))).send_keys('Test')
   
    # Email
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40email2"))).send_keys('sblahut@geekhive.com')
   
    # Country
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40country2"))).send_keys('Test')
   
    # State
    state = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40state2")))
    driver.execute_script("arguments[0].click();", state)
    # Select new york
    newYork = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40state2 > option:nth-child(34)")))
    driver.execute_script("arguments[0].click();", newYork)

    # Company name
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40company2"))).send_keys('Geekhive')
   
    # Newsletter
    optIn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gcdc-field-e915701d-cddc-4a47-bdad-438221c43f40Single_Opt_In")))
    driver.execute_script("arguments[0].click();", optIn)

    print('....Submitting form....')
    print("                                          ")
    # Submit form
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#gate-e915701d-cddc-4a47-bdad-438221c43f40_form_1612992148821 > div.gcdc-submit-button-wrapper.gcdc-form-group.gcdc-form-group-padded > input"))).send_keys('Test')
   
# Call Methods
test_abcWorldCourierIncidentCalculator ()
test_abcWorldCourierSubmitForm ()

print("##########################################")
print("############## Test Complete #############")
print("Total Run Time of Script: " + str(datetime.datetime.now() - scriptStart))
print("##########################################")
print("                                          ")

#Test is complete
#driver.quit()

################################################################################################
############### World Courier Site Automation Incident Calculator Test Script ##################
################################################################################################