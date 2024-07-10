from selenium import webdriver #importing  the web driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options #call the options library
options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #.get = call the website
driver.maximize_window()
print(driver.title)
# driver.find_element(By.CSS_SELECTOR,"input[value='radio2']").click() # this command is used to click the radio button by using CSS selector locator
# time.sleep(5)
# driver.find_element(By.CSS_SELECTOR,"input[value='radio3']").click()
# time.sleep(10)
# driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
# driver.find_element(By.CSS_SELECTOR,"input.radioButton[value='radio2']").click()
     #