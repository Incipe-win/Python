import requests
import re
import time
import json


class LeiHan:
    def __init__(self):
        self.url = "https://wengpa.com/neihan/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
        self.content = []

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        print(response.status_code)
        return response.content.decode()

    def parse_text(self, str_html, page):
        if page <= 5:
            regular = r"<p><strong>.*?</strong>(.*?)</p>"
            self.content.append(re.findall(regular, str_html, re.S))
        else:
            regular = r"<p>(.*?)</p>"
            self.content.append(re.findall(regular, str_html, re.S))

    def save_text(self):
        #  print(self.content)
        with open("leihan.txt", "a", encoding="utf-8") as f:
            for content in self.content:
                for data in content:
                    f.write(data)
                    f.write("\n")

    def run(self):
        page = 1
        while page != 3:
            url = self.url.format(page)
            print(url, end=" ")
            str_html = self.parse_url(url)
            self.parse_text(str_html, page)
            # print(self.content)
            page += 1
        self.save_text()


if __name__ == "__main__":
    leihan = LeiHan()
    leihan.run()
