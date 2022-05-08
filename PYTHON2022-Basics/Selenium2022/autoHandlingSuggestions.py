from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(3)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
#print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
# verify if India is selected by text serch
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
