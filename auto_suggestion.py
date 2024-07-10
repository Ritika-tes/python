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
search_box = driver.find_element("xpath","//input[@name='q']") #here searchbox is a variable
search_box.send_keys("one plus headphone")  #here we search the product name one plus headphones
time.sleep(2)
#first_option = driver.find_element("xpath","(//form[@action='/search']//a[1])").click()
first_option = driver.find_element("xpath","((//form[contains(@class,'header-form')]//a)[1])").click()
