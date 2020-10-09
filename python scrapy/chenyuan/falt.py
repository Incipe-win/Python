import requests
from selenium import webdriver
import time
from lxml import etree


class Table:
    def __init__(self):
        self.url = "http://58.47.143.9:2045/zfca/login"

    def simulate(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        driver.find_element_by_id("username").send_keys("2018052653")
        driver.find_element_by_id("password").send_keys("fuck0907.")
        driver.find_element_by_class_name("btn_dl").click()
        driver.implicitly_wait(7)
        driver.find_element_by_id("157889641106043279").click()
        cookies = driver.get_cookies()
        cookies = {i["name"] + "=" + i["value"] for i in cookies}
        cookies = ";".join(i for i in cookies)
        url = self.parse_url(cookies)
        # new_window = "window.open(url)"
        # driver.execute_script(new_window)
        # driver.switch_to_window(driver.window_handles[1])
        time.sleep(2)
        driver.quit()

    def parse_url(self, cookies):
        url = "http://58.47.143.9:6031/xs_main.aspx?xh=2018052653"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
            "Cookie": cookies
        }
        response = requests.get(url, headers=headers)
        print(response.content.decode())
        html = etree.HTML(response.content.decode())
        ret = html.xpath("//ul/li[4]/ul/li[1]/a/@href")
        print(ret)
        return ret

    def run(self):
        self.simulate()


if __name__ == "__main__":
    table = Table()
    table.run()
