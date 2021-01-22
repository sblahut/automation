#Import driver for Chrome
from selenium import webdriver

#Needed to add wait steps
import time
#Needed to create a new DIR
import os

#Open Chrome
driver = webdriver.Chrome("./chromedriver.exe")
driver.set_window_size(1920, 1080)

#Loading message
print("....Navigating to the Bon & Viv webpage...")

#Open page and wait...
driver.get("https://abi-stage-bonviv.adobecqms.net/en/privacy-policy.html")  
time.sleep(1)
driver.execute_script("window.scrollTo(0, window.scrollY + 400)")

###############################################################################################
#                        URL Validation Removed                                               #
###############################################################################################


#Validation for pulling the proper URL: http://abi-dev-bonviv.adobecqms.net/en/privacy-policy.html
#if driver.current_url == "http://abi-dev-bonviv.adobecqms.net/en/privacy-policy.html":
#   print("Success!")
#else:
#    print("404")

###############################################################################################
#                        Directory Creation Removed                                           #
###############################################################################################

# Create directory
#dirName = 'validation-screenshots'
#try:
    # Create target Directory
#    os.mkdir(dirName)
#    print("Directory " , dirName ,  " Created ") 
#except FileExistsError:
#    print("Directory " , dirName ,  " already exists")

# Character correction for URLs
chars = [':','/','%'] #add more if needed

# PRE CHANGE
image_name = '.\\validation-screenshots\\'+driver.current_url+'_before_validation.png'

#POST CHANGE
#image_name = '.\\validation-screenshots\\'+driver.current_url+'after_validation.png'

for char in chars:
    image_name = image_name.replace(char,'_')
#Saves a screenshot to your computer.
driver.save_screenshot(image_name)

#Close the browser
driver.close()
