from selenium import webdriver #importing  the web driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #call the options library
options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.find_element(By.ID,"checkBoxOption1").click() #use to find element to locate and click on option1
# driver.find_element(By.ID,"checkBoxOption2").click()
driver.find_element(By.ID,"radio1").click()