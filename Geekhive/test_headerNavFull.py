import unittest
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

GeekhiveEnvironmentLink = "https://www.geekhive.com/"
expectedPageLoadTimeInSeconds = 3

headerNavLinks = {
    "Home": GeekhiveEnvironmentLink,
    "Services":GeekhiveEnvironmentLink + "services",
    "Customer Experience":GeekhiveEnvironmentLink + "services/customer-experience",
    "Data, Analytics, & Visualization":GeekhiveEnvironmentLink + "services/data-analytics-visualization",
    "Content Marketing":GeekhiveEnvironmentLink + "services/content-marketing",
    "Technology":GeekhiveEnvironmentLink + "services/technology",
    "Industries":GeekhiveEnvironmentLink + "industries",
    "Thinking":GeekhiveEnvironmentLink + "thinking",
    "Work":GeekhiveEnvironmentLink + "work",
    "Partners":GeekhiveEnvironmentLink + "partners",
    "Company":GeekhiveEnvironmentLink + "about",
    "Events":GeekhiveEnvironmentLink + "events",
    "Press Releases":GeekhiveEnvironmentLink + "press-releases",
    "Careers":GeekhiveEnvironmentLink + "careers",    
    "Contact":GeekhiveEnvironmentLink + "contact",
}


#Record Script Start Time for Script Duration
scriptStart = datetime.now()

#Initialize browser to get to webpage
driver = webdriver.Chrome("./chromedriver")
driver.set_window_size(1920, 1080)


TestsPass = 0
TestsFail = 0
TestsWarning = 0

#################################Test Case ############################################

for key in headerNavLinks:
    print("....resetting to homepage...")
    driver.get(GeekhiveEnvironmentLink)  
    time.sleep(1.5) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = headerNavLinks[key]

    

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""
    ExternalLink = False
    if len(driver.window_handles) == 1: #Same tab
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
    else: #New Tab
        driver.switch_to.window(driver.window_handles[1])
        ExternalLink = True
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    
    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Hyperlink text: " + linkText)
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


























    #Back Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(-1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

    #External links open up second tabs.  Let's see if this link goes external:
    
        if driver.current_url == GEHAEnvironmentLink:
            testResult = "Pass"
            currentTab = driver.current_url
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    



    #Record Results
    print("********Back Button Navigation Results**********")
    print("Url to navigate to: " + GEHAEnvironmentLink)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Forward Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(+1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

        #Verify it went to the correct page
        if driver.current_url == expectedURL:
            testResult = "Pass"
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    #Record Results
    print("********Forward Button Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


for key in footerLinksCol2:
    print("....resetting to homepage...")
    driver.get(GEHAEnvironmentLink)  
    time.sleep(1) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = footerLinksCol2[key]

    
    footerElements = driver.find_elements_by_class_name("footer-list")
    LinkElement = footerElements[1].find_element_by_xpath(".//*[contains(text(), '" + linkText + "')]")

    #Simulate hover event
    elementActions = ActionChains(driver).move_to_element(LinkElement)
    elementActions.perform()
    time.sleep(.5)

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""
    ExternalLink = False
    if len(driver.window_handles) == 1: #Same tab
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
    else: #New Tab
        driver.switch_to.window(driver.window_handles[1])
        ExternalLink = True
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    
    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Hyperlink text: " + linkText)
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Back Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(-1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

    #External links open up second tabs.  Let's see if this link goes external:
    
        if driver.current_url == GEHAEnvironmentLink:
            testResult = "Pass"
            currentTab = driver.current_url
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    



    #Record Results
    print("********Back Button Navigation Results**********")
    print("Url to navigate to: " + GEHAEnvironmentLink)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Forward Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(+1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

        #Verify it went to the correct page
        if driver.current_url == expectedURL:
            testResult = "Pass"
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    #Record Results
    print("********Forward Button Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


for key in footerLinksCol3:
    print("....resetting to homepage...")
    driver.get(GEHAEnvironmentLink)  
    time.sleep(1) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = footerLinksCol3[key]

    
    footerElements = driver.find_elements_by_class_name("footer-list")
    LinkElement = footerElements[2].find_element_by_xpath(".//*[contains(text(), '" + linkText + "')]")

    #Simulate hover event
    elementActions = ActionChains(driver).move_to_element(LinkElement)
    elementActions.perform()
    time.sleep(.5)

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""
    ExternalLink = False
    if len(driver.window_handles) == 1: #Same tab
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
    else: #New Tab
        driver.switch_to.window(driver.window_handles[1])
        ExternalLink = True
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    
    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Hyperlink text: " + linkText)
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Back Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(-1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

    #External links open up second tabs.  Let's see if this link goes external:
    
        if driver.current_url == GEHAEnvironmentLink:
            testResult = "Pass"
            currentTab = driver.current_url
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    



    #Record Results
    print("********Back Button Navigation Results**********")
    print("Url to navigate to: " + GEHAEnvironmentLink)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Forward Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(+1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

        #Verify it went to the correct page
        if driver.current_url == expectedURL:
            testResult = "Pass"
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    #Record Results
    print("********Forward Button Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1

for key in footerLinksCol4:
    print("....resetting to homepage...")
    driver.get(GEHAEnvironmentLink)  
    time.sleep(1) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = footerLinksCol4[key]

    
    footerElements = driver.find_elements_by_class_name("footer-list")
    LinkElement = footerElements[3].find_element_by_xpath(".//*[contains(text(), '" + linkText + "')]")

    #Simulate hover event
    elementActions = ActionChains(driver).move_to_element(LinkElement)
    elementActions.perform()
    time.sleep(.5)

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""
    ExternalLink = False
    if len(driver.window_handles) == 1: #Same tab
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
    else: #New Tab
        driver.switch_to.window(driver.window_handles[1])
        ExternalLink = True
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    
    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Hyperlink text: " + linkText)
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Back Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(-1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

    #External links open up second tabs.  Let's see if this link goes external:
    
        if driver.current_url == GEHAEnvironmentLink:
            testResult = "Pass"
            currentTab = driver.current_url
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    



    #Record Results
    print("********Back Button Navigation Results**********")
    print("Url to navigate to: " + GEHAEnvironmentLink)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Forward Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(+1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

        #Verify it went to the correct page
        if driver.current_url == expectedURL:
            testResult = "Pass"
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    #Record Results
    print("********Forward Button Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1

for key in footerLinksCol5:
    print("....resetting to homepage...")
    driver.get(GEHAEnvironmentLink)  
    time.sleep(1) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = footerLinksCol5[key]

    
    footerElements = driver.find_elements_by_class_name("footer-list")
    LinkElement = footerElements[4].find_element_by_xpath(".//*[contains(text(), '" + linkText + "')]")

    #Simulate hover event
    elementActions = ActionChains(driver).move_to_element(LinkElement)
    elementActions.perform()
    time.sleep(.5)

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""
    ExternalLink = False
    if len(driver.window_handles) == 1: #Same tab
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
    else: #New Tab
        driver.switch_to.window(driver.window_handles[1])
        ExternalLink = True
        if driver.current_url == expectedURL:
            testResult = "Pass"
            currentTab = driver.current_url
            
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


    
    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Hyperlink text: " + linkText)
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Back Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(-1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

    #External links open up second tabs.  Let's see if this link goes external:
    
        if driver.current_url == GEHAEnvironmentLink:
            testResult = "Pass"
            currentTab = driver.current_url
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    



    #Record Results
    print("********Back Button Navigation Results**********")
    print("Url to navigate to: " + GEHAEnvironmentLink)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    #Forward Button Test
    if ExternalLink == False:
        time.sleep(.2)
        testStart = datetime.now()
        driver.execute_script("window.history.go(+1)")
        #Action Completed.  Record time
        testEnd = datetime.now()

        #Verify it retrieved the page in ample time
        testTime = (testEnd - testStart)
        if testTime.seconds > expectedPageLoadTimeInSeconds:
            testResult = "Warning"
            testNotes = "Page load time is slow"

        #Verify it went to the correct page
        if driver.current_url == expectedURL:
            testResult = "Pass"
    else:
        testResult = "Warning"
        testNotes = "External links open in new tabs.  the Next button will not navigate.  Test omitted."

    #Record Results
    print("********Forward Button Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + driver.current_url)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)

    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


for key in SocialLinksDictionary:
    print("....resetting to homepage...")
    driver.get(GEHAEnvironmentLink)  
    time.sleep(1) #Make sure all elements load
    testResult = "Fail"
    testNotes = ""

    #Get link information from link list
    linkText = key
    expectedURL = SocialLinksDictionary[key]

    footerElements = driver.find_elements_by_class_name("footer-social")
    LinkElement = footerElements[0].find_element_by_xpath(".//*[contains(@class, '" + linkText + "')]")
    
    #Simulate hover event
    elementActions = ActionChains(driver).move_to_element(LinkElement)
    elementActions.perform()
    time.sleep(.5)

    #Record Time, click link
    testStart = datetime.now()
    driver.execute_script("arguments[0].click();", LinkElement)

    #Action Completed.  Record time
    testEnd = datetime.now()

    #Verify it went to the correct page
    #External links open up second tabs.  Let's see if this link goes external:
    currentTab = ""

    driver.switch_to.window(driver.window_handles[1])
    currentTab = driver.current_url
    if driver.current_url == expectedURL:
        testResult = "Pass"
    
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    #Verify it retrieved the page in ample time
    testTime = (testEnd - testStart)
    if testTime.seconds > expectedPageLoadTimeInSeconds:
        testResult = "Warning"
        testNotes = "Page load time is slow"

    
        

    #Record Results
    print("********Header Link Navigation Results**********")
    print("Url to navigate to: " + expectedURL)
    print("Actual URL navigated to: " + currentTab)
    print("Navigation time: " + str(testTime))
    print("TestResult: " + testResult)
    print("Test Notes:")
    print("     " + testNotes)
    print("")
    if testResult == "Pass":
        TestsPass += 1
    elif testResult == "Fail":
        TestsFail += 1
    elif testResult == "Warning":
        TestsWarning += 1


    

print("##########################################")
print("########### Overall Script Results #######")
print("##########################################")
print("Number of Pass Results: " + str(TestsPass))
print("Number of Fail Results: " + str(TestsFail))
print("Number of Warnings: " + str(TestsWarning))
print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
print("##########################################")
print("############# Script Complete ############")
print("##########################################")
time.sleep(1)
#Test is complete
driver.quit()
