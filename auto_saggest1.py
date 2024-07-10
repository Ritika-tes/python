from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser 
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://www.flipkart.com/") #.get = call the website
driver.maximize_window()
time.sleep(3)
popup = driver.find_element("xpath","//button[text()='✕']")
time.sleep(3)
popup.click()
search_box = driver.find_element("xpath","//input[@name='q']")  # here search_box is variable,
# xpath of search bar is located
search_box.click()
search_box.send_keys("one plus")
time.sleep(4)
doptions=driver.find_elements("xpath","//form[@action='/search']//a")  # here the autoseggest result
# is stord in variable name doptions
for b in doptions: # here due to multiple numbre of suggetion options we have created list,
                                   # and put it into the variable name b,  where we used the for loop
    if "one plus 11r" in b.text: #here we used if condition to search the suggetion name one plus 11r in variable b
        b.click()                # if it find the suggetion in variable b then it will click on it
        break                    # after that it will automaticlly break the statment.



