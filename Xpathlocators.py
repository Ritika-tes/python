from selenium import webdriver #importing  the web driver
import time
from selenium.webdriver.common.by import By # calling class BY
from selenium.webdriver.chrome.options import Options #call the options class
options = Options() #created the object
options.add_experimental_option("detach",True) #to detach automatically close the web browser
driver = webdriver.Chrome (options=options) # pass the object,opening the chrome browser
driver.get("https://rahulshettyacademy.com/AutomationPractice/") #.get = call the website
driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@value='radio1' and @class='radioButton']").click() #to click the redio one option
# driver.find_element(By.XPATH,"//input[@value='radio2' and @class='radioButton']").click()
# #when ew put (or) instead of (and) it do not click
# any option because redioButtan is comman in all three webelements
#time.sleep(5)
# driver.find_element(By.XPATH,"//input[starts-with(@value,'radio1')]").click() #by using starts-with()
#driver.find_element(By.XPATH,"//input[contains(@value,'io2')]").click() #it shows radio2

#driver.find_element(By.XPATH,"//input[contains(@value,io')]/").click()  #it did click any option becaus multipal elements
# contain io wodriver.find_element(By.XPATH,"//input[starts-with(@name,'radioButton') and contains(@value,'io3')]").click()

#driver.find_element("xpath","//input[starts-with(@name,'radioButton') and contains(@value,'io3')]").click()
#//legend[starts-with(text(),'Suggession')]  # it shows the partial value text which is headline ,but it can not click,so we do not
# need to wright driver.find element

# driver.find_element(By.XPATH,"//div[@id='radio-btn-example']//input[@value='radio2']").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"(//div[@id='checkbox-example']//input)[2]").click()
# #parent to specific number of chaildn or gradchaild

# time.sleep(3)
# driver.find_element("xpath","(//div[@id='radio-btn-example']//input)[3]").click()
# #parent to specific number of chaildn or gradchaild

# variableb=driver.find_element("xpath","//legend[contains(text(),'Button')]")
# #here we have provide a veriable b,which carry xpath locater

# print(variableb.text)  #here we have print the variable and given text command

         # parent to last child or grandchild
# driver.find_element("xpath","(//div[@id='checkbox-example']//input)[last()]").click()

         # parent to second last or third last child
#driver.find_element("xpath","(//div[@id='checkbox-example']//input)[last()-1]").click()

        #child to any ancestor
#driver.find_element("xpath","//input[@value='radio3']/ancestor::div[@id='radio-btn-example']").click()
# #here compiler said that proccess finished with exit code 0,it means the query has been successfully executed
# ,but it did not reflected on webpage,because there is not any click option

        #parent to first 'n' number of child
#driver.find_element("xpath","(//div[@id='checkbox-example']//input)[position()<3]").click()
# #here if we write less than 3 then it will show only 1 not 2 becaus it shows only one option at a time

# driver.find_element("xpath","(//div[@id='checkbox-example']//input)[position()=2]").click()
# it will show the second position only


driver.find_element("xpath","(//div[@id='checkbox-example']//input)[position()>2]").click()
# here we use ID to find loction of the webelement which will click only one radio
# buttan at a time which is less than 2 is only 1

