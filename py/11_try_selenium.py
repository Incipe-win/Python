from selenium import webdriver
import time

# 创建对象
driver = webdriver.Chrome()
# 过时
# driver = webdriver.PhantomJS()
# 设置窗口大小
# driver.set_window_size(1920, 1080)
# 最大化窗口
driver.maximize_window()

# 获取请求
driver.get("https://www.baidu.com")

# driver.save_screenshot("./baidu.png")

# 元素定位方法
# driver.find_element_by_id("kw").send_keys("python")
# driver.find_element_by_id("su").click()

# 获取html
print(driver.page_source)

# 获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("*" * 100)
# cookies = {i["name"]: i["value"] for i in cookies}
# print(cookies)

# close
time.sleep(1)
driver.quit()
