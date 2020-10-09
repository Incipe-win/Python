import requests
from selenium import webdriver
import time
from lxml import etree
from selenium.webdriver.chrome.options import Options


class Table:
    def __init__(self):
        self.url = "http://58.47.143.9:2045/zfca/login "
        # self.number = number
        # self.passwd = passwd

    def simulate(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')  # 这个配置很重要
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        # driver.find_element_by_id("username").send_keys(self.number)
        # driver.find_element_by_id("password").send_keys(self.passwd)
        driver.find_element_by_id("username").send_keys("2018052682")
        driver.find_element_by_id("password").send_keys("bingmei1235789")
        driver.find_element_by_class_name("btn_dl").click()
        time.sleep(1)
        driver.find_element_by_id("157889684646655577").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        # driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(1)
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/ul/li[4]/a/span").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/ul/li[4]/ul/li[1]/a").click()
        time.sleep(1)
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(1)
        html = etree.HTML(driver.page_source)
        size = html.xpath(
            'count(/html/body/form/div[3]/div/div[2]/div/div[1]/select/option)')
        size = int(size)
        commond = "document.getElementById('{}').options[{}].selected = true;"
        for j in range(size):
            html = etree.HTML(driver.page_source)
            id_lists = html.xpath("//td/select/@id")
            for i in id_lists:
                if i == "DataGrid1_JS1_14" or i == "DataGrid1_JS2_14":
                    end = commond.format(i, 2)
                else:
                    end = commond.format(i, 1)
                driver.implicitly_wait(7)
                # time.sleep(1)
                driver.execute_script(end)
            try:
                time.sleep(2)
                # driver.implicitly_wait(7)
                driver.find_element_by_name("Button1").click()
            except Exception as e:
                driver.refresh()
                time.sleep(1)
                driver.find_element_by_name("Button1").click()
            else:
                print("success")

        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element_by_name("Button2").click()
        time.sleep(1)
        driver.quit()

    def run(self):
        self.simulate()


if __name__ == "__main__":
    # number = input("input your id: ")
    # passwd = input("input your passwd: ")
    # table = Table(number, passwd)
    table = Table()
    table.run()
