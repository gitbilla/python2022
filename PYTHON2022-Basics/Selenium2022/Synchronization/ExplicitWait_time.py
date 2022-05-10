from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

# find the element using css
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(4)
# Validate if we could get the products
# find the element using css
count1 = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert  count1 == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

# all the items are added
# using css
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located(By.CLASS_NAME, "promoCode"))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(expected_conditions.presence_of_all_elements_located(By.CSS_SELECTOR, "span.promoInfo"))

# using selenium waits
print(driver.find_element_by_css_selector("span.promoInfo").text)



#assert count1 == 3
"""
c = (driver.find_elements_by_xpath("//div[@class='product']/div"))
for i in c:
    print(i)
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print(count)

"""

