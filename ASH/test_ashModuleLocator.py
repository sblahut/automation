################################################################################################
############# American Society of Hematology Site Automation Module Locator Script #############
################################################################################################

# The 'element' variable will determine which web element you are trying to locate on the webpage. 

from selenium import webdriver
import time
from datetime import datetime
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Declare Chrome Driver Vairable
driver = webdriver.Chrome("./chromedriver")

# Wait
driver.implicitly_wait(15)

# Results Declaration
TestsPass = 0
TestsFail = 0
TestsWarning = 0
testResult = ""

# Record Script Start Time for Script Duration
scriptStart = datetime.now()

# Loading message
print("....Navigating to the American Society of Hematology webpage...")

# Pull ASH Homepage
driver.get('http://www.hematology.org/')


def test_module_locator():
     
  try:
    
    # Set the element in which you want to find here.
    element = driver.find_element_by_css_selector("#search > span.search-label > i")
    
    # Condition if element is found

    if element.is_displayed():
      print("#########################################")
      print("############# Module Found! #############")
      print("#########################################")
      print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
      print("#########################################")
  # Condition if element is not found
  except NoSuchElementException:
    print("#########################################")
    print("########### No Module Found! ############")
    print("#########################################")
    print("Total Run Time of Script: " + str(datetime.now() - scriptStart))
    print("#########################################")

# Call Method
test_module_locator()

# Wait
time.sleep(1)

#Test is complete
driver.quit()

################################################################################################
############# American Society of Hematology Site Automation Module Locator Script #############
################################################################################################