from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://accounts.douban.com/passport/login")
driver.get("https://www.douban.com/")
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.find_element_by_class_name("account-tab-account").click()
driver.find_element_by_id("username").send_keys("17775676477")
driver.find_element_by_id("password").send_keys("www.12345.com")

driver.find_element_by_class_name("account-form-field-submit ").click()

cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)

time.sleep(60)
driver.quit()
