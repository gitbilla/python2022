from selenium import webdriver
import time

"""
https://www.rahulshettyacademy.com/AutomationPractice/
https://rahulshettyacademy.com/dropdownsPractise/
https://rahulshettyacademy.com/seleniumPractise/#/  # vegetables
https://jqueryui.com/menu/
"""

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
#driver.find_element_by_name("name").send_keys('Abraham')
#driver.find_element_by_name("email").send_keys('Abraham@gmail.com')
#driver.find_element_by_class_name('form-check-input').click()

# using css selector for name
#CSS syntax from browser console $x("input[@type='submit']")
#tagname[atttribute='value']
#input[name='name']
driver.find_element_by_css_selector("input[name='name']").send_keys("Abraham")

# using name selector for email
driver.find_element_by_name("email").send_keys('Abraham.billa@gmail.com')
# using class selector for check box
driver.find_element_by_class_name('form-check-input').click()

# DROP down options
# Select class provides the method to handle the options in dropdown
dropdown = Select(driver.find_elements_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(0) # return again to select Male


# using XPATH selector for Submit button
# syntax for xpath
# //tagname[@attribute=value]
#input[@type='submit']   # from browser/console  $x("//input[@type='submit']")
## //input[@type='submit']
driver.find_element_by_xpath("//input[@type='submit']").click()

# extracing text from web page with Validations
print(driver.find_element_by_class_name("alert-success").text)



