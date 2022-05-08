from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element_by_css_selector("input[name='q']").send_keys("American Lifestyle")
driver.find_element_by_css_selector("input[class='gNO89b']").submit()

