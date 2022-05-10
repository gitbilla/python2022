from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.implicitly_wait(5)
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
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

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

