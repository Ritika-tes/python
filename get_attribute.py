from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.maximize_window()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# c=driver.find_element("xpath","//a[@class='blinkingText']") #here veriable c is created which contains the locater which find the xpath of link
# print(c.get_attribute("href")) #here the print function is used to show the link in below terminal
# c.click()  # in this we give the clickfunction to the variable c



#=====================================prohtam 2 ===============================================
driver.get("https://www.flipkart.com/")
popup = driver.find_element("xpath","//button[text()='✕']")  #here we take a popup as veriable
time.sleep(3)
popup.click()
d=driver.find_elements("xpath","//div[@data-clone='false']//a") #here we find the xpath for the image link
print(f"total number of image link:{len(d)} ")
for e in d :  #here we created new e veriable which is scaning variable d,variable d contains 4 image links
    print(e.get_attribute("href")) #here we print the variable e with the help of locater
    # get_attribute which find attribut href carru whole link as a value
