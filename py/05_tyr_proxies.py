import requests

proxies = {
    "http": "http://115.223.7.110:80"
}

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

response = requests.get("http://www.baidu.com",
                        proxies=proxies, headers=headers)
print(response.status_code)
