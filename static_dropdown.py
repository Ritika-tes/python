from selenium import webdriver #importing  the web driver
import time
from selenium.webdriver.common.by import By # calling class BY
from selenium.webdriver.chrome.options import Options #call the options class
from selenium.webdriver.support.select import Select

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #.get = call the website
driver.maximize_window()
static_dropdown = driver.find_element(By.ID,"dropdown-class-example")
a = Select(static_dropdown)
a.select_by_index(2)  #here we select the value by its index
time.sleep(5)
a.select_by_value("option3")  # here we have selected the value by attribut value
time.sleep(5)
a.select_by_visible_text("Option1")  #here we have select the value by the text seen on website




