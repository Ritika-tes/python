from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css") ### here we call the wbsite
driver.maximize_window() #maximaise the window
fram1 = driver.find_element("xpath","//iframe[@id='iframeResult']") # we find the xpath of principle/parent  fram
# which carrys all the 3 frams within it
driver.switch_to.frame(fram1) # we say to the driver to switch from parent fram to chaild frame
driver.switch_to.frame(0) ### here we have to select fist frame hence, we have to provide index number 0
driver.find_element("xpath","//a[@title='Login to your account']").click() ## after switching to first frame, we find the
# xpath of the login buttan
time.sleep(8)

