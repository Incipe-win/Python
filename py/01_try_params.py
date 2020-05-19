# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
# p = {"wd": "传智博客"}
#
# url_temp = "https://www.baidu.com/s?"
#
# response = requests.get(url_temp, headers=headers, params=p)
# print(response.status_code)
# print(response.request.url)

url = "https://www.baidu.com/s?wd={}".format("传智博客")
# url = "https://www.baidu.com"
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.request.url)
# print(response.content.decode())
