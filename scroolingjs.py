from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://en.wikipedia.org/wiki/Python_(programming_language)")

# page scroll by pixel

driver.execute_script('window.scrollBy(0,3000)',"")
time.sleep(5)

# scroll down to specific element
ele = driver.find_element("xpath","//span[text()='Programming examples']")
driver.execute_script("arguments[0].scrollIntoView()",ele)
time.sleep(4)



#### scroll down at the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
time.sleep(4)


#### scroll upside by pixel
driver.execute_script('window.scrollBy(0,-3000)',"")
time.sleep(5)



######  scroll up at the top
driver.execute_script("window.scrollTo(0,0)","")
time.sleep(4)


