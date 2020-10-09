import requests
import threading
import json
import re
from pprint import pprint
import time


class DuiTan:
    def __init__(self):
        self.url_list = ["https://www.duitang.com/napi/blog/list/by_album/?album_id=218516&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start=24&_=1589856959421",
                         "https://www.duitang.com/napi/blog/list/by_album/?album_id=218516&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start=48&_=1589856959422",
                         "https://www.duitang.com/napi/blog/list/by_album/?album_id=218516&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start=72&_=1589856959423",
                         "https://www.duitang.com/napi/blog/list/by_album/?album_id=218516&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start=96&_=1589856959424",
                         "https://www.duitang.com/napi/blog/list/by_album/?album_id=218516&limit=24&include_fields=top_comments%2Cis_root%2Csource_link%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Creply_count&start=120&_=1589856959425"]
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

    def parse_url(self, url):
        print("*" * 20)
        response = requests.get(url, headers=self.headers)
        return response.content

    def get_img_url(self, ret):
        img_list = []
        for dic in ret["data"]["object_list"]:
            img_list.append(dic["photo"]["path"])
        return img_list

    def regular(self, strs):
        ret = re.findall(
            r"https://c-ssl.duitang.com/uploads/item/.*?_(.*?)\.(.*?)$", strs, re.M | re.S)
        print(ret)
        return ret

    def download_imgs(self, img_url_list):
        for img_url in img_url_list:
            img = self.parse_url(img_url)
            time.sleep(3)
            strs = self.regular(img_url)
            with open("./duitan/{}.{}".format(strs[0][0], strs[0][1]), "wb") as f:
                f.write(img)
            print("{} success".format(img_url))

    def run(self):
        for url in self.url_list:
            json_str = self.parse_url(url).decode()
            ret = json.loads(json_str)
            img_url_list = self.get_img_url(ret)
            thread = threading.Thread(
                target=self.download_imgs, args=(img_url_list, ))
            thread.start()


if __name__ == "__main__":
    duitan = DuiTan()
    duitan.run()
