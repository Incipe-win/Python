import pprint
import requests
from lxml import etree
import json
from parse_url_png import parse_url
import threading
import time
import re


def regular(strs):
    return re.findall(r"http://cdn.weitoupiao.com/image/1/.*?/(.*?)\.(.*?)/small", strs, re.M | re.S)


def download_png():
    for png_url in ret:
        png = parse_url(png_url)
        time.sleep(1)
        strs = regular(png_url)
        print(strs)
        with open("./img/{}.{}".format(strs[0][0], strs[0][1]), "wb") as f:
            f.write(png)
        print("save success!")


url = "http://www.weitoupiao.com/example/w8std7gnrvvsf.html?alllink=/"
html_str = parse_url(url)
html = etree.HTML(html_str)
ret = html.xpath("//div[@class=\"vote-item-cover\"]/img/@src")
thread = threading.Thread(target=download_png)
thread.start()
