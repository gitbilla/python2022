from selenium import  webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[2]/input[1]").send_keys("Abraham")
driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[4]/input[1]").send_keys("Augustine")
driver.find_element_by_css_selector("#userEmail").send_keys("Abraham@gmail.com")
driver.find_element_by_xpath("//label[contains(text(),'Other')]").click()
driver.find_element_by_css_selector("#userNumber").send_keys("1234567890")


dateofbirth = driver.find_element_by_css_selector("#dateOfBirthInput").click()
time.sleep(2)
dateofbirth = driver.find_element_by_css_selector("#dateOfBirthInput").clear()
driver.find_element_by_css_selector("#dateOfBirthInput").send_keys("12 May 1980")
#driver.switch_to.frame(dateofbirth)



driver.find_element_by_xpath("//label[contains(text(),'Sports')]").click()


time.sleep(2)
#driver.quit()




"""
radio = driver.find_element_by_css_selector("input[value='radio1']").is_selected()
print(radio)
driver.find_element_by_css_selector("input[value='radio1']").click()
radio = driver.find_element_by_css_selector("input[value='radio1']").is_selected()
print(radio)
driver.quit()
"""
