import requests
import threading
import json
import re
from pprint import pprint
import time


class Bing:
    def __init__(self):
        self.url = "https://bing.ioliu.cn/?p={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    def parse_url(self, url):
        print("*" * 20)
        response = requests.get(url, headers=self.headers)
        return response.content

    def regular_img_name(self, img_url):
        ret = re.findall(
            r"http://h1.ioliu.cn/bing/(.*?)\.(.*?)$", img_url, re.M | re.S)
        print(ret)
        return ret

    def download_imgs(self, img_list):
        for url in img_list:
            img = self.parse_url(url)
            time.sleep(1)
            strs = self.regular_img_name(url)
            with open("./bing/{}.{}".format(strs[0][0], strs[0][1]), "wb") as f:
                f.write(img)
            print("{} success".format(url))

    def regular_img_url(self, html_str):
        ret = re.findall(r".*?pic=(.*?)\?imageslim.*?", html_str, re.M | re.S)
        return ret

    def run(self):
        for i in range(1, 141):
            url = self.url.format(i)
            html_str = self.parse_url(url).decode()
            img_list = self.regular_img_url(html_str)
            print(img_list)
            thread = threading.Thread(
                target=self.download_imgs, args=(img_list, ))
            thread.start()


if __name__ == "__main__":
    bing = Bing()
    bing.run()
