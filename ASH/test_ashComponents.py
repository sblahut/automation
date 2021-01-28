################################################################################################
######### American Society of Hematology Site Automation Hidden Components Test Script #########
################################################################################################

######### This test is setup on a page level basis #########
######### The test would need to be setup for each subdomain #########
######### It will only scan the entered URL #########

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

def test_allAshComponents():

    # Results declaration
    visibleFound = 0
    hiddenFound = 0
    idsFound = 0
    noIDFound = 0

    print('....Navigating to www.hematology.org/....')

    # Open ash website
    driver.get('https://hematology.org/')
    
    ids = driver.find_elements_by_xpath('//*[@id]')
    
    for id in ids:

        title = id.get_attribute('title')
        cssClass = id.get_attribute('class')
        href = id.get_attribute('href')
        hidden = id.get_attribute('hidden')

        print("                                          ")
        print("##########################################")
        # Search by ID.
        if id.get_attribute('id') != "":
            print("ID: " + id.get_attribute('id'))
            idsFound += 1
        else:
            noIDFound += 1       
        # Search by A HREF.
        if (href) != None:
            print("Link: " + str(href))
        # Search by Title.
        elif (title) != "":
            print("Title: " + str(title))
        # Search by Class.
        elif (cssClass) != "":
            print("Class: " + str(cssClass))
        # Search by Visibility.
        elif (hidden) != None:
            print("Hidden: " + str(hidden))
        # Visibility status check
        if id.is_displayed():
            print("Visual Check: Visible")
            visibleFound += 1
        else:
            print("Visual Check: Hidden")
            hiddenFound += 1
        print("##########################################")
        print("                                          ")
    print("##########################################")
    print("######### HEMATOLOGY.ORG RESULTS #########")   
    print("Number of Element IDs Found: " + str(idsFound))
    print("Number of Elements with No ID Found: " + str(noIDFound))
    print("Number of Visible Elements: " + str(visibleFound))
    print("Number of Hidden Elements: " + str(hiddenFound))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("                                          ")

# Call Method
test_allAshComponents()

# Wait
time.sleep(1)

#Test is complete
driver.quit()            


################################################################################################
######### American Society of Hematology Site Automation Hidden Components Test Script #########
################################################################################################