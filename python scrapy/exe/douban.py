import json
import requests
import pprint
import time


class DouBan:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
        }
        self.proxies = {"https": "https://58.220.95.79:10000"}
        # self.proxies = dict(http='socks5://127.0.0.1:7891',
        #                     https='socks5://127.0.0.1:7891')
        print(self.proxies)

    def judge(self, ret):
        result = True if len(ret["subjects"]) < 20 else False
        return result

    def save_content(self, ret, pages):
        pages //= 20
        with open("./res/{}doubantv.json".format(pages), "w", encoding="utf-8") as f:
            f.write(json.dumps(ret, ensure_ascii=False, indent=2))

    def joint(self, pages):
        return self.url.format(pages)

    def run(self):
        pages = 0
        while True:
            url = self.joint(pages)
            response = requests.get(
                url, headers=self.headers, proxies=self.proxies)
            print("{}success!".format(pages // 20), end=" ")
            print("url is {}".format(url))
            html_str = response.content.decode()
            print(html_str)
            ret = json.loads(html_str)
            isEmpty = self.judge(ret)
            if isEmpty == True:
                break
            else:
                self.save_content(ret, pages)
                pages += 20
                time.sleep(10)


if __name__ == "__main__":
    url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}"
    douban = DouBan(url)
    douban.run()
