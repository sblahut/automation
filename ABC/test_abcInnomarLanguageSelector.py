################################################################################################
################### Innomar Site Automation Language Selector Test Script ######################
################################################################################################

import requests
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Declare Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

scriptStart = datetime.datetime.now()

print("                                          ")
print('....Navigating to Innomar Home Page....')
print("                                          ")

# Open innomar website
driver.get('https://www.innomar-strategies.com/')
# Accept Cookies
#driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

def test_abcInnomarLanguageSelector ():

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()
    
    # Select French
    print("....Changing language to French....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(2)"))).click()  

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("########## Test Case #1: French ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select English
    print("....Changing language to English....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(1)"))).click()  

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #2: English ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "            #####")
    print("##########################################")
    print("                                          ")
    
# Call Methods
test_abcInnomarLanguageSelector ()

print("##########################################")
print("############## Test Complete #############")
print("Total Run Time of Script: " + str(datetime.datetime.now() - scriptStart))
print("##########################################")
print("                                          ")

#Test is complete
driver.quit()  

################################################################################################
################### Innomar Site Automation Language Selector Test Script ######################
################################################################################################