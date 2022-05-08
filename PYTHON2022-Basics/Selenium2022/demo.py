from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/')
print('title of the web page:', driver.title)
print(driver.current_url)
time.sleep(3)
driver.get('https://www.rahulshettyacademy.com/#/practice-project')
driver.minimize_window()
driver.back()
driver.refresh()
time.sleep(5)
driver.close()