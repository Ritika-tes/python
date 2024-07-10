from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("rprpratrit@gmail.com")
time.sleep(5)
driver.find_element(By.ID,"pass").send_keys("Ritika@39")
time.sleep(10)
driver.find_element(By.NAME,"login").click()
time.sleep(15)

