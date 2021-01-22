#This tells your python script that you are going to use selenium:
from selenium import webdriver

#This tells your python script that you are going to use time based stuff.
import time

#This tells your python script that you are going to do neat things like hover and stuff:
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains







#This will tell selenium to open a browser window at a specific size.  It may take a moment....
driver = webdriver.Chrome("./chromedriver")
driver.set_window_size(1920, 1080)

#Print something to the window
print("....Navigating to the geekhive webpage...")

#Navigate to a webpage and wait for the elements to load
driver.get("https://www.geekhive.com/careers")  
time.sleep(1) 

#This next part is where most of the time is spent when doing automation.
#You must 'search' the page for any elements with a specific property.  
#If you inspect the careers hyperlink, it is an <a) with the text "Careers"
#
#There can be multiple places that have the text 'Careers'.  To make sure we get the right one, we will narrow it down by finding the parent element.
#The Parent element is a <div> with a class="footer__content".
#There is only one element with the text 'Careers' in the div 'footer__content'


#Find the parent element and return all of the elements under it to 'FooterLinks'
FooterLinks = driver.find_elements_by_class_name("header")
#FooterLinks now contains all of the elements in the div "footer__content"

#Lets find the first (and only) element in the 'footer__content' that has the text 'Careers'
CareerHyperlink = FooterLinks[0].find_element_by_xpath(".//*[contains(text(), 'Weightlifting')]")



#This moves a fake mouse to the Careers hyperlink and hovers over it.
elementActions = ActionChains(driver).move_to_element(CareerHyperlink)
elementActions.perform()
time.sleep(2)

#click on the hyperlink!!!!
driver.execute_script("arguments[0].click();", CareerHyperlink)

#See what URL the browser is on:
print(driver.current_url)

#We want it to navigate to https://www.geekhive.com/careers.  Let's see if it did:
if driver.current_url == "https://www.geekhive.com/careers":
    print("Yay!")
else:
    print("boo!")


#Close the browser
driver.close()
