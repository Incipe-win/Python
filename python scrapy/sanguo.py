import requests
import re
from pprint import pprint
import pandas as pd
import jieba
import matplotlib.pyplot as plt
import wordcloud


class BiliBili:
    def __init__(self):
        self.url = "https://api.bilibili.com/x/v1/dm/list.so?oid=197711172"
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
        data_frame = pd.DataFrame(strs, columns=["弹幕内容"])
        data_frame.to_csv("sanguo.csv", encoding="utf-8")
        # print(data_frame)
        # with open("xiyou.txt", "w", encoding="utf-8") as f:
        #     for content in strs:
        #         f.write(content)
        #         f.write("\n")
        # print("save success")

    def word_cloud(self, strs):
        words = ",".join(strs)
        words_list = jieba.lcut(words)
        words_strs = "".join(words_list)
        # words_strs = ",".join(strs)
        image = plt.imread("./unnamed.jpg")
        wc = wordcloud.WordCloud(
            background_color="white",
            mask=image,
            font_path="./STXINGKA.TTF",
            max_words=6000,
            max_font_size=100,
            min_font_size=10,
            random_state=50,
        )
        word_cloud = wc.generate(words_strs)
        word_cloud.to_file("sanguo.png")

    def run(self):
        html_str = self.parse_url()
        strs = self.regular(html_str)
        self.save_strs(strs)
        self.word_cloud(strs)


if __name__ == "__main__":
    bilibili = BiliBili()
    bilibili.run()
