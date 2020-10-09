import requests
import re
import sys

query_string = sys.argv[1]

headers = {
    "User-Agent":
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36"
}

post_data = {
    "inputtext": query_string,
    "type": "AUTO"
}

post_url = "http://m.youdao.com/translate"

response = requests.post(post_url, data=post_data, headers=headers)
res_str = r'<li>(.*?)</li>'
html_str = response.content.decode()
m_str = re.findall(res_str, html_str, re.S | re.M)
value_list = []
for value in m_str:
    value_list.append(value)
print("Translate result is: ", end="")
print(value_list[-1])
