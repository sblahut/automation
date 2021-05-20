################################################################################################
#################### Securos Site Automation Product Catalog Test Script #######################
################################################################################################

import os
import datetime
from itertools import islice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

# Declare Chrome Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

scriptStart = datetime.datetime.now()

print('....Navigating to Securos Product Detail Page....')
print("                                          ")
print("##########################################")
print('####### Checking PDP Page Layout #########')
print("                                          ")
# Open securos website
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
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-wishlist-modal__inner-content-container > div > div > div:nth-child(2) > div:nth-child(1) > div.product-wishlist-modal__quantity > div > input.product-wishlist-modal__quantity--plus"))).click()
    print('....Adding another one to the wish list....')
    print("                                           ")

    # Add another one to the wish list
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-wishlist-modal__inner-content-container > div > div > div:nth-child(2) > div:nth-child(1) > div.product-wishlist-modal__quantity > div > input.product-wishlist-modal__quantity--plus"))).click()
    print('....Adding another one to the wish list....')
    print("                                           ")

    # View wish list
    view = driver.find_element(By.CSS_SELECTOR, "#product-wishlist-modal__inner-content-container > div > div > div:nth-child(2) > div:nth-child(1) > div.product-wishlist-modal__wrapper > a.product-wishlist-modal__button.button-primary")
    driver.execute_script("arguments[0].click();", view)
    print('....Viewing the wish list....')
    print("                                           ")

    # Accept Cookies
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(3) > div.legal-acknowledgement.background-true-blue > div > div > div > div > form > button"))).click()

    # Removing one from the wish list

    remove = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div.wishlist-listing__item > div.wishlist-listing__quantity > div > div.wishlist-listing__quantity-form > input.wishlist-listing__quantity--minus")
    driver.execute_script("arguments[0].click();", remove)
    print('....Removing one from the wish list....')
    print("                                           ")

    # Run Results
    ids = driver.find_elements(By.CLASS_NAME, "wishlist-listing__product-content")
    wishListQuantity = driver.find_elements(By.XPATH, "/html/body/div[1]/main/div/div[2]/div[4]/div/div/div/div[1]/div[2]/div/div[1]/label/input")

    print("##########################################")
    print("####### TEST CASE: PRINT WISH LIST #######")
    
    for id in islice(ids, 0, 3, 1):
        
        print("Item: " + str(id.text))
        for item in wishListQuantity:
            print("Quantity: " + str(item.get_attribute('value')))
            testCaseResult = str(item.get_attribute('value'))
            print("##########################################")
            if int(testCaseResult) == 2:
                print('### RESULT: ############ PASS ############')
            else:
                print('### RESULT: ############ FAIL ############')
    print("##########################################")
    print("                                          ")

    # Request Quote
    requestQuote = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > div:nth-child(4) > div > div > div > div.wishlist-listing__buttons > div.wishlist-listing__buttons__left > a.wishlist-listing__buttons__button.button-primary")
    driver.execute_script("arguments[0].click();", requestQuote)
    print('....Requesting a quote....')
    print("                                           ")

    # Run Results
    expectedURL = 'https://www.securos.com/catalog-selector/us-product-catalog/order-form'

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(3) > main > div > div.content__middle > form > button")))
    
    print("##########################################")
    print("######## TEST CASE: REQUEST QUOTE ########")
    print("Expected URL: " + expectedURL)
    print("Current URL: " + driver.current_url)
    if driver.current_url == expectedURL:
        print('### RESULT: ############ PASS ############')
    else:
        print('### RESULT: ############ FAIL ############')
    print("##########################################")

# Call Methods
test_abcSecurosProductDetailLayout ()
test_abcSecurosProductWishList ()

print("                                          ")
print("##########################################")
print("############## Test Complete #############")
print("Total Run Time of Script: " + str(datetime.datetime.now() - scriptStart))
print("##########################################")
print("                                          ")

#Test is complete
driver.quit()  

################################################################################################
#################### Securos Site Automation Product Catalog Test Script #######################
################################################################################################