################################################################################################
############# World Courier Site Automation Press Release Filter Test Script ###################
################################################################################################

import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.now()

def test_abcWorldCourierPressReleasesFilter():

    print('....Navigating to www.worldcourier.com/news-and-events/press-releases....')
    print("                                          ")
    print("##########################################")
    print('##### Checking Filter Functionality ######')
    # Open wc website
    driver.get('https://www.worldcourier.com/news-and-events/press-releases')

    # Accept Cookies
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()
    
    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2012
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(9)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    print("                                          ")
    print("##########################################")
    print("############## Results 2012 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")
    
    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2014
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(8)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2014 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2015
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(7)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2015 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2016
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(6)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2016 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2018
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(5)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2018 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2019
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(4)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2019 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click 2020
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(3)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("############## Results 2020 ##############")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

    # Click Dropdown
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select").click()

    # Click Last 6 Months
    driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > main > div > div.content__top > div.marginator.margin-top-2 > form > span > label > select > option:nth-child(2)").click()

    # Run Results
    ids = driver.find_elements_by_class_name('module__body')
    
    print("                                          ")
    print("##########################################")
    print("######### Results Last 6 Months ##########")
    for id in ids:
        
        print("Date: " + str(id.text))
    print("##########################################")
    print("                                          ")

# Call Method
test_abcWorldCourierPressReleasesFilter()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  

################################################################################################
############# World Courier Site Automation Press Release Filter Test Script ###################
################################################################################################