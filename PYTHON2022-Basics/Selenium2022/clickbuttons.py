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
    checkbox.click()
    assert checkbox.is_selected() # verify if checkboxes are selected



