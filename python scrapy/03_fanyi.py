import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
data = {
    "from": "en",
    "to": "zh",
    "query": "hello",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "54706.276099",
    "token": "db1b24fa144367386cdc27b5b106eea2",
    "domain": "common"
}

post_url = "https://fanyi.baidu.com/v2transapi"

response = requests.post(post_url, data=data, headers=headers)
print(response.status_code)
print(response.content.decode())
