################################################################################################
#################### Securos Site Automation Product Catalog Test Script #######################
################################################################################################

import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from itertools import islice

# Set options variable
options = webdriver.ChromeOptions() 

# Maximize window
options.add_argument("start-maximized")

# Disable info bars
options.add_argument('disable-infobars')

# Set chromedriver variable
driver=webdriver.Chrome(chrome_options=options, executable_path=r'./chromedriver')

scriptStart = datetime.datetime.now()

print('....Navigating to Securos Product Detail Page....')
print("                                          ")
print("##########################################")
print('####### Checking PDP Page Layout #########')
print("                                          ")
# Open xcenda website
driver.get('https://www.securos.com/catalog-selector/us-product-catalog/power-equipment/arbutus/sawcover-system/arbutus---sagittal-saw-blade-13mm')
# Accept Cookies
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button").click()

###############################################################################################
#                               Directory Creation                                            #
###############################################################################################

print('....Creating Directory....')
# Create directory
dirName = 'validation-screenshots'
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory" , dirName ,  "created.")
    print("##########################################")
except FileExistsError:
    print("Directory" , dirName ,  "already exists.")
    print("##########################################")

###############################################################################################
#                               Screenshot Capturing                                          #
###############################################################################################
    
def test_abcSecurosProductDetailLayout ():
    
    #Saves a screenshot to your computer.
    timestamp = datetime.datetime.now()
    print("                                          ")
    print('Saving screenshot...  1-Securos-PDP.png')
    print("                                          ")
    driver.save_screenshot('.\\validation-screenshots\\1-Securos-PDP.png')
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

    #Saves a screenshot to your computer.
    timestamp = datetime.datetime.now()
    print("                                          ")
    print('Saving screenshot...  2-Securos-PDP.png')
    print("                                          ")
    driver.save_screenshot('.\\validation-screenshots\\2-Securos-PDP.png')
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

    #Saves a screenshot to your computer.
    timestamp = datetime.datetime.now()
    print("                                          ")
    print('Saving screenshot...  3-Securos-PDP.png')
    print("                                          ")
    driver.save_screenshot('.\\validation-screenshots\\3-Securos-PDP.png')
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

    #Saves a screenshot to your computer.
    timestamp = datetime.datetime.now()
    print("                                          ")
    print('Saving screenshot...  4-Securos-PDP.png')
    print("                                          ")
    driver.save_screenshot('.\\validation-screenshots\\4-Securos-PDP.png')
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

    #Saves a screenshot to your computer.
    timestamp = datetime.datetime.now()
    print("                                          ")
    print('Saving screenshot...  5-Securos-PDP.png')
    print("                                          ")
    driver.save_screenshot('.\\validation-screenshots\\5-Securos-PDP.png')
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

def test_abcSecurosProductWishList ():

    # Add product to wish list
    add = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div.marginator.margin-top-0 > div > div > div > div > div.product-hero__name-description > a")
    driver.execute_script("arguments[0].click();", add)
    print("                                          ")
    print('....Adding to the wish list....')
    print("                                          ")

    # Add another one to the wish list
    addAnother = driver.find_element(By.CLASS_NAME, "product-wishlist-modal__quantity--plus")
    driver.execute_script("arguments[0].click();", addAnother)
    print("                                           ")
    print('....Adding another one to the wish list....')
    print("                                           ")

    # Add another one to the wish list
    driver.execute_script("arguments[0].click();", addAnother)
    print("                                           ")
    print('....Adding another one to the wish list....')
    print("                                           ")

    # View wish list
    view = driver.find_element(By.CSS_SELECTOR, "#product-wishlist-modal__inner-content-container > div > div > div:nth-child(2) > div:nth-child(1) > div.product-wishlist-modal__wrapper > a.product-wishlist-modal__button.button-primary")
    driver.execute_script("arguments[0].click();", view)
    print("                                           ")
    print('....Viewing the wish list....')
    print("                                           ")

    # Removing one from the wish list
    remove = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div.wishlist-listing__item > div.wishlist-listing__quantity > div > div.wishlist-listing__quantity-form > input.wishlist-listing__quantity--minus")
    driver.execute_script("arguments[0].click();", remove)
    print("                                           ")
    print('....Removing one from the wish list....')
    print("                                           ")

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "wishlist-listing__product-content")
    
    print("                                          ")
    print("##########################################")
    print("########## Test Case: Wish List #########")
    for id in islice(ids, 0, 3, 1):
        
        print("Address: " + str(id.text))
    print("##########################################")
    print("                                          ")

# Call Methods
test_abcSecurosProductDetailLayout ()
test_abcSecurosProductWishList ()

#Test is complete
driver.quit()  

################################################################################################
#################### Securos Site Automation Product Catalog Test Script #######################
################################################################################################