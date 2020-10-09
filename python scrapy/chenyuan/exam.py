import json
import requests
from pprint import pprint
import time
import threading


class Answer:
    def __init__(self):
        self.url = "https://hncu.xuetangx.com/api/score/result/E+24823+0007-{}/?offset=0&limit=60"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Cookie": "plat_id=231; org_id=392; mode=1; xt=gAAAAABe4DNWaTtnzZ7bfnjoPNi8CdUOZZi2nYOgb78Uqf8NWN5sAeN5vUYZCRvMyRtRLNptsNaaHt0tsvXagda0v70RKlvMJSPaKwriZNsAnGRVP7hBfEk; xt_expires_in=604800; identity=1; access_token=gAAAAABe4XPNHN6PjMjHgU1SvCEhJrbeKvXSbvN7RFum1tyOE2uoPK7CdcBH-UALB30XuQFOcbgWMNz1irMPBQL2etPZfoMMaUBPON_qyEF67OmzjipmXY4"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        print(url + " " + str(response.status_code))
        return response.content.decode()

    def save_content(self, content):
        ret = json.loads(content)
        dic = ret["data"]
        print(len(dic))
        with open("./exam.txt", "a+", encoding="utf-8") as f:
            for data in dic:
                f.write(data["stem"])
                f.write("\n")
                f.write(str(data["correct_answer"]))
                f.write("\n")
                f.write("\n")

    def get_url_list(self):
        return [self.url.format(i) for i in range(1, 101)]

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            content = self.parse_url(url)
            print(content)
        # thread = threading.Thread(
        #     target=self.save_content, args=(content, ))
        # thread.start()
        # time.sleep(1)


if __name__ == "__main__":
    answer = Answer()
    answer.run()
