from selenium import webdriver
import time # we us this command to provide time.sleep in ferther code

from selenium.webdriver.chrome.options import Options

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.maximize_window()

####======================================== to capture the screnshot of specific webelement====================================================================
driver.get("https://the-internet.herokuapp.com/upload")  #we get the link
# h=driver.find_element("id","file-upload")  ## here we find locater id of which screenshot we have to find
# h.screenshot(".\\test.png")   ### . is used for to save a screenshot in current folder/directory where all programs are saved.
### we can choose the path where we want to save the screenshot


########================================================== To capture the screenshot of whole website =======================================================================


#driver.save_screenshot(".\\test1.png")  ## here we used inbuld function is save_screenshort, and provide name to the file test1 ,it is save in drive c
# driver.save_screenshot("C:\pythonselenium\pythonproject\screenshort\\test2.png")  ## here we used .save_screenshot function and provide the
##provide the path of saving the file


driver.get_screenshot_as_file("C:\pythonselenium\pythonproject\screenshort\\test3.png")  ### here we use .get_screenshot_as_
# file function to capture the screenshot
