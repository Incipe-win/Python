import requests
from time import sleep
from multiprocessing import Pool
from pprint import pprint
# 本声明:每次使用前都需要去修改cookie值(有时间限制，每个cookie最多可以使用半天)


class course():
    header = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'plat_id=231; org_id=392; mode=1; xt_expires_in=604800; identity=1; access_token=gAAAAABevjIiNK8SAGJwtZvp3iuq3cR9WuunLN-xtuAR2ho9-1YAIBMPU1mPaIeHwS6rw4OARFIJfdtVWtz0wzRn-pB5XOm-IsroL5yu8R5sd_8AMkPXKDk; xt=gAAAAABevjIiYafET6LIUjTQ5GWV9gYSFNmDz3Su4de2dDNEWnHHBWJ9a8usap12RSpAQCgIxytReFpVvRnFt7MwchrusxZ6ahfia84X-I-ddJA5BzqQGyk',
        'Host': 'hncu.xuetangx.com',
        'If-Modified-Since': '0',
        'Referer': 'https://hncu.xuetangx.com/lms',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'xtbz': 'cloud',
    }
    length_dict = {}

    def get_length(self, cid):
        url = "https://hncu.xuetangx.com/video_point/get_video_watched_record?cid={}&vtype=rate&video_type=video".format(
            cid)
        response = requests.get(url, headers=self.header)
        response = response.json()
        return response

    def view_media(self, page, length, cid):
        rate = 15  # 视频播放速率
        count = int(length / rate) + 1
        for it in range(1, count):
            getData = {'i': '5',
                       'et': 'heartbeat',
                       'p': 'web',
                       'n': 'cc',
                       'lob': 'cloud3',
                       'cp': it * rate,
                       'fp': '0',
                       'tp': '0',
                       'sp': '3',
                       'ts': '1587610719249',
                       'u': 951274,
                       'c': cid,
                       'v': page,
                       'cc': page,
                       'd': length,
                       'pg': '{}_qeuv'.format(page),
                       'sq': it,
                       't': 'video',
                       '_': '1587610506121', }
            response = requests.get(
                "https://hncu.xuetangx.com/heartbeat", params=getData, headers=self.header)
            sleep(1)
            print(response.text)
        print('*' * 80)

    def start(self):
        cid = input("请输入你要刷的课程ID号:")
        self.length_dict = self.get_length(cid)
        pool = Pool(7)
        self.list = list(self.length_dict.keys())
        for it in self.list:
            length = self.length_dict['{}'.format(it)]['video_length']
            pool.apply_async(self.view_media, args=(it, length, cid))
        pool.close()
        pool.join()


if __name__ == '__main__':
    brain = course()
    brain.start()
