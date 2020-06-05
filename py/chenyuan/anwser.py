import json
import requests
from pprint import pprint
import time
from retrying import retry
import threading


class Answer:
    def __init__(self):
        self.url = "https://hncu.xuetangx.com/inner_api/homework/score/result/H+24823+{}/H+24823+{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Cookie": "plat_id=231; org_id=392; mode=1; xt=gAAAAABe0u185WRTDJZ4M7s8MKbwiAmob7v1NUOC_NffRWARo5HPAAJCyrXNnGda-9EwWn0Kc0C6yoLOyKrlyB9_BNA1LYYidHuYFhzbPkk5KWyqXa64dTA; xt_expires_in=604800; identity=1; access_token=gAAAAABe2jaQL5TY-1Z-4b6lnK_SFpPPTDi2G_fCM4Q5AJMyB7mietgMiaUrnkEkAM4-7g2DsXgGPnlKXozxJYcVlr9tzERYpG52qw7PRnZM7dLnAVej-HM"
        }

    @retry(stop_max_attempt_number=3)
    def _parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=3)
        print(url + " " + str(response.status_code))
        assert response.status_code == 200
        return response.content.decode()

    def parse_url(self, url):
        print(url)
        try:
            html_str = self._parse_url(url)
        except:
            html_str = None
        return html_str

    def save_content(self, content):
        ret = json.loads(content)
        dic = ret["data"]
        data_list = ret["data"]["question_data"]
        with open("./anwser.txt", "a+", encoding="utf-8") as f:
            f.write(dic["name"])
            f.write("\n")
            for data in data_list:
                f.write(data["stem"])
                f.write("\n")
                f.write(str(data["correct_answer"]))
                f.write("\n")
                f.write("\n")

    def run(self):
        for i in range(1, 164):
            print(i, end=" ")
            new_url = self.url.format(str(i).zfill(3), str(i).zfill(3))
            content = self.parse_url(new_url)
            thread = threading.Thread(
                target=self.save_content, args=(content, ))
            thread.start()
            time.sleep(1)


if __name__ == "__main__":
    answer = Answer()
    answer.run()
