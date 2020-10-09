#! /usr/bin/python3.8
import requests
import sys
from selenium import webdriver
import time
from lxml import etree


class Table:
    def __init__(self, number_id, passwd):
        self.url = "http://58.47.143.9:2045/zfca/login "
        self.number_id = number_id
        self.passwd = passwd

    def simulate(self):
        # 启动
        driver = webdriver.Chrome()
        # 最大化
        driver.maximize_window()
        # 地址请求
        driver.get(self.url)
        # 登录
        driver.find_element_by_id("username").send_keys(self.number_id)
        driver.find_element_by_id("password").send_keys(self.passwd)
        driver.find_element_by_class_name("btn_dl").click()
        time.sleep(1)
        # 进入教务系统
        driver.find_element_by_id("157889684646655577").click()
        # 切换到最新的页面
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        time.sleep(1)
        # 切换到测评页面
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/ul/li[4]/a/span").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div[1]/div[2]/ul/li[4]/ul/li[1]/a").click()
        time.sleep(1)
        # 有frame，需要转换
        driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
        time.sleep(1)
        # 计算有多少门课要测评
        html = etree.HTML(driver.page_source)
        size = html.xpath(
            'count(/html/body/form/div[3]/div/div[2]/div/div[1]/select/option)')
        size = int(size)
        # 利用js完成选项
        commond = "document.getElementById('{}').options[{}].selected = true;"
        for j in range(size):
            # 找到每一门课程有多少个评价
            time.sleep(1)
            html = etree.HTML(driver.page_source)
            id_lists = html.xpath("//td/select/@id")
            for i in id_lists:
                # 防止评价重复
                if i == "DataGrid1_JS1_14" or i == "DataGrid1_JS2_14":
                    end = commond.format(i, 2)
                else:
                    end = commond.format(i, 1)
                driver.implicitly_wait(7)
                # time.sleep(1)
                driver.execute_script(end)
            try:
                time.sleep(2)
                driver.find_element_by_name("Button1").click()
            except Exception as e:
                driver.refresh()
                time.sleep(2)
                driver.find_element_by_name("Button1").click()
            else:
                print("success")
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        driver.find_element_by_name("Button2").click()
        time.sleep(5)
        driver.quit()
        print("---end----")

    def run(self):
        print("---start----")
        self.simulate()


if __name__ == "__main__":
    if len(sys.argv) == 3:
        number_id = sys.argv[1]
        passwd = sys.argv[2]
    else:
        print("./文件名 学籍号 密码")
        sys.exit()
    table = Table(number_id, passwd)
    table.run()
