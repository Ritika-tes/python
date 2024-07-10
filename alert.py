from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
h = driver.find_element("xpath","//iframe[@id='iframeResult']")
driver.switch_to.frame(h)

#accept alert ============================================
# driver.find_element("xpath","//button[@onclick='myFunction()']").click()
# time.sleep(3)
# driver.switch_to.alert.accept()


##to dismiss alert===============================================
# driver.find_element("xpath","//button[@onclick='myFunction()']").click()
# time.sleep(3)
# driver.switch_to.alert.dismiss()

### to write a text in alert=========================================
driver.find_element("xpath","//button[@onclick='myFunction()']").click()
time.sleep(1)
driver.switch_to.alert.send_keys("thanks for giving alert")
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(3)