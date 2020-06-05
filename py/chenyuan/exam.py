import json
import requests
from pprint import pprint
import time
import threading


class Answer:
    def __init__(self):
        self.url = "https://hncu.xuetangx.com/api/score/result/E+24823+0004-56/?offset=0&limit=1000"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Cookie": "plat_id=231; org_id=392; mode=1; xt=gAAAAABe0u185WRTDJZ4M7s8MKbwiAmob7v1NUOC_NffRWARo5HPAAJCyrXNnGda-9EwWn0Kc0C6yoLOyKrlyB9_BNA1LYYidHuYFhzbPkk5KWyqXa64dTA; xt_expires_in=604800; identity=1; access_token=gAAAAABe2jaQL5TY-1Z-4b6lnK_SFpPPTDi2G_fCM4Q5AJMyB7mietgMiaUrnkEkAM4-7g2DsXgGPnlKXozxJYcVlr9tzERYpG52qw7PRnZM7dLnAVej-HM"
        }

    def parse_url(self):
        response = requests.get(self.url, headers=self.headers)
        print(self.url + " " + str(response.status_code))
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

    def run(self):
        content = self.parse_url()
        thread = threading.Thread(
            target=self.save_content, args=(content, ))
        thread.start()
        time.sleep(1)


if __name__ == "__main__":
    answer = Answer()
    answer.run()
