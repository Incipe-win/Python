import requests
import re
from pprint import pprint


class BiliBili:
    def __init__(self):
        self.url = "https://api.bilibili.com/x/v1/dm/list.so?oid=155377309"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    def parse_url(self):
        response = requests.get(self.url, headers=self.headers)
        print(response.status_code)
        return response.content.decode()

    def regular(self, html_str):
        rule = r"<d p=.*?>(.*?)</d>"
        strs = re.findall(rule, html_str, re.M | re.S)
        return strs

    def save_strs(self, strs):
        with open("bilibili.txt", "w", encoding="utf-8") as f:
            for content in strs:
                f.write(content)
                f.write("\n")
        print("save success")

    def run(self):
        html_str = self.parse_url()
        strs = self.regular(html_str)
        self.save_strs(strs)


if __name__ == "__main__":
    bilibili = BiliBili()
    bilibili.run()
