################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
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

def test_abcInnomarClinicLocator ():



# Call Method
test_abcInnomarClinicLocator ()

# Wait
time.sleep(1)

#Test is complete
driver.quit()  
















################################################################################################
################### Innomar Site Automation Clinic Locator Test Script #########################
################################################################################################