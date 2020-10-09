import requests
import re


class Video():
    def __init__(self, url):
        self.url = "https://jiexi.380k.com/?url={}&type=".format(url)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    def parse_url(self):
        print(self.url)
        response = requests.get(self.url, headers=self.headers)
        print(response.status_code)
        return response.content.decode()

    def run(self):
        content = self.parse_url()
        print(content)


if __name__ == "__main__":
    url = "https://v.qq.com/x/cover/0s8n49g3g1rv1oz/l0034jn1hzh.html"
    video = Video(url)
    video.run()
