from selenium import webdriver
import time # we us this command to provide time.sleep in ferther code

from selenium.webdriver.chrome.options import Options

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")  #we get the link
fileInput=driver.find_element("id",'file-upload') # we find the xpath of the chuse file and stored inside the variable of fileInput
fileInput.send_keys(r"D:\Flipkart.png")  # we chose file from computers for that we use send keys function
a=driver.find_element("id",'file-submit') # we find xpath of submit button and stored in variable a
a.click()             # click on variable a

