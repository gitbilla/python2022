from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://jqueryui.com/checkboxradio/")
driver.maximize_window()

driver.find_element_by_xpath("//body/div[1]/fieldset[1]/label[1]").click()