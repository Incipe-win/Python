import requests

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"""}

url = "https://www.weibo.com/login.php"

response = requests.get(url, headers=headers)

fo1 = open("1.txt", "w")
fo2 = open("2.txt", "w")

fo1.write(response.text)
fo2.write(response.content.decode())
fo1.close()
fo2.close()
# print(response.text)
# print('*' * 80)
# print(response.content.decode())
