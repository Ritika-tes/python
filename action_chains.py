import time

from selenium import webdriver
from selenium.webdriver import ActionChains # importing action chains class

from selenium.webdriver.chrome.options import Options

options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.maximize_window()
# driver.get("https://seleniumbase.io/demo_page")
# a=driver.find_element("id","myDropdown") #we locate the webelement using locater "id",and stored in variable a
# time.sleep(2)
# b=driver.find_element("id","dropOption2")  #we locate the webelement using locater "id",and stored in variable b
# achains = ActionChains(driver)   # here we call actionchain class and inside the bracket we have to mentioned mandatory "driver",
# #  and stored actionchain function in achains variable
# achains.move_to_element(a).move_to_element(b).click().perform()   # here we use move to element function to move the curser of mouse on the specific webelement
# #whenever we used move_to_element,drage and drop element,context element we have to put perform function at the end
#




#####=========================================== right click =========================================================================

driver.get("https://demo.guru99.com/test/simple_context_menu.html")
# right_click=driver.find_element("xpath","//span[text()='right click me']")
# achains = ActionChains(driver)
# achains.context_click(right_click).perform() # we put the right click veriable inside the context_click function

####=============================================== double click ======================================================================================

d_click = driver.find_element("xpath","//button[text()='Double-Click Me To See Alert']")
achains = ActionChains(driver)
achains.double_click(d_click).perform()  #here we put d_click veriable into double click function

######==============================================  drage and drop =================================================================================
#
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# e=driver.find_element("id","box3")
# f=driver.find_element("id","box103")
# dd=ActionChains(driver)
# dd.drag_and_drop(e,f).perform()


