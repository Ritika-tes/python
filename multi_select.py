from selenium import webdriver
import time
from selenium.webdriver.common.by import By # calling class BY
from selenium.webdriver.chrome.options import Options #call the options class
from selenium.webdriver.support.select import Select

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://omayo.blogspot.com/") #.get = call the website
driver.maximize_window()
multi_selecter = driver.find_element("id","multiselect1") # here multiselecter is a variable which used to acces xpath locater
b = Select(multi_selecter)

b.select_by_index(1)
time.sleep(3)
b.select_by_value("volvox")
time.sleep(3)
b.select_by_visible_text("Audi")
time.sleep(5)
b.deselect_by_index(0)
time.sleep(3)
b.deselect_all()

# when we locate the path attribut id must be mandetary most of the time we have to select the attribut id
# in the select by index,value or visible text