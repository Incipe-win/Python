import requests
import re
from pprint import pprint
import pandas as pd
import jieba
import matplotlib.pyplot as plt
import wordcloud


class BiliBili:
    def __init__(self):
        self.url = "https://api.bilibili.com/x/v1/dm/list.so?oid=207809223"
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
        data_frame.to_csv("tenxun.csv", encoding="utf-8")
        # print(data_frame)
        # with open("xiyou.txt", "w", encoding="utf-8") as f:
        #     for content in strs:
        #         f.write(content)
        #         f.write("\n")
        # print("save success")

    def word_cloud(self, strs):
        # print(strs)
        # words = ",".join(strs)
        # print(words)
        # words_list = jieba.lcut(words)
        # for i in words_list:
        #     if i == ',' or i == '!' or i == '(' or i == ')':
        #         words_list.remove(i)
        # print(words_list)
        # words_strs = ",".join(words_list)
        # print(words_strs)
        words_strs = ",".join(strs)
        # words_strs = str(words_list)
        # print(words_strs)
        image = plt.imread("./images.png")
        wc = wordcloud.WordCloud(
            background_color="white",
            mask=image,
            font_path="./STXINGKA.TTF",
            max_words=6000,
            max_font_size=60,
            min_font_size=6,
            random_state=50,
        )
        word_cloud = wc.generate(words_strs)
        word_cloud.to_file("tenxun5.png")

    def run(self):
        html_str = self.parse_url()
        strs = self.regular(html_str)
        self.save_strs(strs)
        self.word_cloud(strs)


if __name__ == "__main__":
    bilibili = BiliBili()
    bilibili.run()
