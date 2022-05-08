from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()

driver.find_element_by_css_selector("#username").send_keys("Abraham Billa")
driver.find_element_by_css_selector("#password").send_keys("Billa@123")
driver.find_element_by_css_selector("#password").clear()

# handling liks ex : forget password
driver.find_element_by_link_text("Forgot Your Password?").click() # valid only when this is a link

# Generating Xpath based on text
# we will cancel the forgotten url and return to the login page
# syntax //tagname[text()='text']
#driver.find_element_by_xpath("//a[text()='Cancel']").click()  # verified the xpath from console $x("//a[text()='Cancel']")
driver.find_element_by_css_selector("input[name='cancel'").click()  # this method is css and working
#driver.find_element_by_xpath("//a[text()='Cancel']").click() # not working

# creating Xpath and CSS by Traversing tags