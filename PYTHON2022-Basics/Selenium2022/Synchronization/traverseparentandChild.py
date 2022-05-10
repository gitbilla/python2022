from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=in")
#driver.maximize_window()

driver.find_element_by_id("username").send_keys("Abraham")
driver.find_element_by_css_selector(".password").send_keys("Abraham")
driver.find_element_by_id("Login").click()

# forgot password
driver.find_element_by_link_text("Forgot Your Password?").click()
# click on cancel
time.sleep(2)
driver.find_element_by_css_selector("input[name='cancel']").click()
driver.find_element_by_xpath("//form[@name='login']/div[1]/label")