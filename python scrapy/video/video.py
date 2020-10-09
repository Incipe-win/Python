import requests
import json
from lxml import etree
from pprint import pprint


class Video:
    def __init__(self, video_url):
        self.url = "https://jiexi.380k.com/?url=" + video_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    def parse_url(self):
        response = requests.get(self.url)
        print(response.status_code)
        return response.content.decode()

    def run(self):
        print(self.url)
        html_str = self.parse_url()
        print(html_str)
        html = etree.HTML(html_str)
        print(url)


if __name__ == "__main__":
    video = Video("https://v.qq.com/x/cover/0s8n49g3g1rv1oz/w003423oudl.html")
    video.run()
