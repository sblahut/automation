################################################################################################
################ World Courier Site Automation Language Selector Test Script ###################
################################################################################################

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from itertools import islice
from bs4 import BeautifulSoup
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
print('....Navigating to World Courier Home Page....')
print("                                          ")

# Open world courier website
driver.get('https://www.worldcourier.com/')
# Accept Cookies
#driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

def test_abcWorldCourierLanguageSelector ():

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()
    
    # Select Portuguese
    print("....Changing language to Portuguese....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(1)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######## Test Case #1: Portuguese ########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select Spanish
    print("....Changing language to Spanish....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(2)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #2: Spanish ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select Chinese
    print("....Changing language to Chinese....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(3)"))).click()  

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #3: Chinese ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select Korean
    print("....Changing language to Korean....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(4)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("########## Test Case #4: Korean ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select Japanese
    print("....Changing language to Japanese....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(5)"))).click() 

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #5: Japanese #########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select French
    print("....Changing language to French....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(6)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("########## Test Case #6: French ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select Russian
    print("....Changing language to Russian....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(7)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #7: Russian ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select German
    print("....Changing language to German....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(8)"))).click() 

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("########## Test Case #8: German ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "         #####")
    print("##########################################")
    print("                                          ")

    # Select language selector
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > header > div > div > div.header-right-column > div > div.header-languages > button").click()

    # Select English
    print("....Changing language to English....")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#languages > a:nth-child(9)"))).click()

    # Run Results
    html = requests.get(driver.current_url).content
    soup = BeautifulSoup(html, 'html.parser')
    print("                                          ")
    print("##########################################")
    print("######### Test Case #9: English ##########")
    print("##### Detect Language: " + str(soup.html["lang"]) + "            #####")
    print("##########################################")
    print("                                          ")
    
# Call Methods
test_abcWorldCourierLanguageSelector ()

print("##########################################")
print("############## Test Complete #############")
print("Total Run Time of Script: " + str(datetime.datetime.now() - scriptStart))
print("##########################################")
print("                                          ")

#Test is complete
driver.quit()  

################################################################################################
################ World Courier Site Automation Language Selector Test Script ###################
################################################################################################