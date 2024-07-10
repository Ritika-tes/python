from selenium import webdriver #importing  the web driver
import time
from selenium.webdriver.common.by import By # calling class BY
from selenium.webdriver.chrome.options import Options #call the options class
options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #.get = call the website
driver.maximize_window()
# check_boxes=driver.find_elements("xpath","//input[starts-with(@id,'checkBoxOption')]")
# print(check_boxes) # here it declares list,we print the variable
# print(len(check_boxes)) # it shows the length of the webelement present in website
# for a in check_boxes: #in checkboxes variable we add 'a' as a element,option1,2,3 will store in a element
#     a.click()  # now in a element,the checkboxes variables values will click
#


######### if we have to select first two options then the following program will be ;
# check_boxes=driver.find_elements("xpath","(//input[starts-with(@value,'option')])[position()<3]")
# print(check_boxes) # here it declares list,we print the variable
# print(len(check_boxes)) # it shows the length of the webelement present in website
# for b in check_boxes:
#     if check_boxes.index(b)+1<3:
#         b.click()
#


###### if we have to chose option1 abd option3 then the following program will be ;
check_boxes=driver.find_elements("xpath","(//input[starts-with(@value,'option')])[position()<=3]")
print(check_boxes) # here it declares list,we print the variable
print(len(check_boxes)) # it shows the length of the webelement present in website
for b in check_boxes:
    if check_boxes.index(b)+1!=2:
        b.click()
