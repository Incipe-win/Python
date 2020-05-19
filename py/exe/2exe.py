import requests

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}
string = input("请输入要查找的内容: ")
page = 0

for i in range(0, 500, 50):
    page += i
    url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&{}".format(string, page)
    files = "tieba{}.txt".format((i // 50 + 1))
    response = requests.get(url, headers=headers)
    print(response.status_code)
    fo = open(files, "w")
    fo.write(response.text)
fo.close()
