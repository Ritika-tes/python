# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
#
# options = Options() #created the object
# options.add_experimental_option("detach",True) #to detach automatically close the web browser
# driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
# driver.maximize_window()
# driver.get("https://www.yatra.com/") # here we call the website with the help of get()
# parent_handle = driver.current_window_handle # current_window_handle is function which represent current window present on brawser
# # which is starting  web page of yatra.com
# # and we stored that window inside a variable called parent_handle
# print(parent_handle) # here we print that page in output we can see id of that window (BE82EC66283007782026D9570EF262D)
# driver.find_element("xpath","//img[@class='conta iner']").click() # here we find the xpath of the another
# # window which is webelement of the previous window
# all_handles = driver.window_handles # in the variable of all_handle we stored the first two windows id and link
# # driver.find_element("xpath","//a[@href='https://www.yatra.com/offer/details/akasa-air-offer']//span[@class='wfull offer-content anim']//span[@class='details wfull bxs']//span[@class='flL view mt10']//span[@class='view-btn flR anim'][normalize-space()='View Details']").click()
# for w in all_handles: # here we applay for loop by taking the variable w,this variable w is  present in all handles variable which contains window
#     # pages of both windows 1st one is main page of yatra.com and another one is webelements window od the fist page
#     if w != parent_handle:  #if w is not equal to parent handle which is first window of yatra.com
#         driver.switch_to.window(w) # then it will swich to second window link
#         driver.find_element("xpath","//a[@href='https://www.yatra.com/offer/details/akasa-air-offer']//span[@class='wfull offer-content anim']//span[@class='details wfull bxs']//span[@class='flL view mt10']//span[@class='view-btn flR anim'][normalize-space()='View Details']").click()
#             #here we find the xpath of the 3rd window which is webelement of second window
#         time.sleep(4) # this page will remain on screen for 4 second
#         driver.close()  # here we clouse the loop
#         break           # here we break a loop
# driver.switch_to.window(parent_handle) ###this command is used to go to the initial 1st window page of yatra.com which is carryed by variable parent_handle
#
#
#
#
#############=======================================================================================================================


from selenium import webdriver
import time
driver = webdriver.Chrome() # pass the object,opening the chrome browser
driver.maximize_window()
driver.get("https://www.yatra.com/") # here we call the website with the help of get()
time.sleep(3)
driver.find_element("xpath","(//img[@class='conta iner large-banner'])[2]").click()
time.sleep(5)

# multipal_windowa = driver.find_element("xpath","//input[@name='email']")

# multipal_windowa.send_keys("Ritika")



