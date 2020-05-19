from lxml import etree
from parse_url_png import parse_url
import requests
import re
import threading
import time


class DuiTan:
    def __init__(self):
        self.raw_url = "https://www.duitang.com/album/?id=218516#!albumpics-p{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    def parse_content_url(self, page):
        url = self.raw_url.format(page)
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_img_list(self, html_str):
        html = etree.HTML(html_str)
        return html.xpath("//a[@class=\"a\"]/img/@src")

    def regular(self, strs):
        print(strs)
        ret = re.findall(
            r"https://c-ssl.duitang.com/uploads/item/.*?_(.*?)\.thumb.400_0\.(.*?)$", strs, re.M | re.S)
        return ret

    def download_img(self, img_list):
        for img_url in img_list:
            img = parse_url(img_url)
            time.sleep(3)
            strs = self.regular(img_url)
            with open("./duitan/{}.{}".format(strs[0][0], strs[0][1]), "wb") as f:
                f.write(img)
            print("./duitan/{}.{} success!".format(strs[0][0], strs[0][1]))

    def run(self):
        page = 1
        while page != 21:
            page += 1
            html_str = self.parse_content_url(page)
            img_list = self.get_img_list(html_str)
            thread = threading.Thread(
                target=self.download_img, args=(img_list, ))
            thread.start()
        # print(img_list)
        # print(len(img_list))


if __name__ == "__main__":
    duitan = DuiTan()
    duitan.run()
