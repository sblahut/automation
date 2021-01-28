################################################################################################
########## American Society of Hematology Site Automation URL Status Code Test Script ##########
################################################################################################

######### This test is setup on a domain level basis #########
######### It will scan all subdomains from the entered URL #########

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

def test_allAshLinks():
    # Results declaration
    TestsFound = 0
    TestsNotFound = 0
    TestsRedirect = 0
    TestsIgnored = 0
    brokenLinks = []

    print('....Navigating to www.hematology.org/....')
    # Open ash website
    driver.get('https://hematology.org/')

    # Declare variable to extract all links
    all_links = [link.get_attribute("href") for link in driver.find_elements_by_xpath("//a[@href]")]

    # Declare variable to separate duplicates found
    unique_links = list(dict.fromkeys(all_links))

    # Number of links found
    print("Number of links : %s" %len(all_links))

    for link in unique_links:

        # If condition is met: run status code
        if link.startswith("https://www.hematology.org/"):
            req = requests.head(link)
            print("_____ Link: " + link + " _____ Status Code: _____ ", req.status_code)


        # If condition is met: run status code
        elif link.startswith("http://www.hematology.org/"):
            req = requests.head(link)
            print("_____ Link: " + link + " _____ Status Code: _____ ", req.status_code)


        # Ignore if previous conditions are not met
        else:
            print("Ignoring external link: '{}'".format(link))
            # Tally external links
            TestsIgnored += 1
        
        # Tally results
        if req.status_code == 200:
            TestsFound += 1
        elif req.status_code == 404:
            TestsNotFound += 1
            # If link is broken, add to broken links list
            brokenLinks.append(str(link))
        elif req.status_code == 301:
            TestsRedirect += 1
    
    # Final tally of results
    print("                                          ")
    print("##########################################")
    print("############# ASH Link Results ###########")
    print("##########################################")
    print("Number of Pass Results: " + str(TestsFound))
    print("Number of Fail Results: " + str(TestsNotFound) + "*")
    print("Number of 301 Redirects: " + str(TestsRedirect))
    print("Number of External Links: " + str(TestsIgnored))
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("##########################################")
    print("############## Test Complete #############")
    print("##########################################")
    print("                                          ")
    print("############## Broken Links ##############")
    for link in brokenLinks:
        print(link)
    print("##########################################")
    print("                                          ")

# Call Method
test_allAshLinks()

# Wait
time.sleep(1)

#Test is complete
driver.quit()            


################################################################################################
########## American Society of Hematology Site Automation URL Status Code Test Script ##########
################################################################################################