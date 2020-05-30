import json
import requests
from pprint import pprint
import time
import threading


class Answer:
    def __init__(self):
        self.url = "https://hncu.xuetangx.com/inner_api/homework/score/result/H+24823+{}/H+24823+{}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Cookie": "plat_id=231; org_id=392; mode=1; xt_expires_in=604800; identity=1; frontendUserReferrer=https://www.xuetangx.com/cloud; frontendUserTrack=52887; _log_user_id=0b3604af9dffb16b69bc828ef652a846; sharesessionid=9464c3228dae2bcb340d9169a0095683; xt=gAAAAABe0OCNbN5XNNKoDC26J_0jCwjobEj3L25QC0oz3umKNcnyyW1xItVJ8QzTBWi7euOY0pG40lZzIDb3mpegGtZUPbTrB4fK2dUteLUzuLJmUKJogng; access_token=gAAAAABe0f6_kUaaGcVQbElyJ_YUUyp_OhCaoVgON8_INq9c8i6NkZElqcCw6VpxQjXH8zbhyEH_Smgsk9nuDwfZVSB1lfENg7tDZtNaJItdEkcuuHKdR1Q"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        print(url + " " + str(response.status_code))
        return response.content.decode()

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
