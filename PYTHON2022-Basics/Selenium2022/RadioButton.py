from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# using xpath
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))
# loop to check all the checkboxes

for checkbox in checkboxes:
    #print(checkbox.get_attribute('value'))
    if checkbox.get_attribute('value') == "option2":
        checkbox.click()
        assert checkbox.is_selected()

# Selecting Radio Button # using xpath or name to find element
# Using xpath method
radiobutton = driver.find_elements_by_xpath("//input[@name='radioButton']") #  using xpath
radiobutton[1].click()
assert radiobutton[1].is_selected()

# Using name method
"""
radiobutton = driver.find_elements_by_name("radioButton") #  using name
radiobutton[2].click()
assert radiobutton[2].is_selected()
"""










