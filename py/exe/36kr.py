import requests
import json
import re
from parse_url import parse_url

url = "https://36kr.com/"
html_str = parse_url(url)

ret = re.findall(r"<script>window.initialState=(.*?)</script>", html_str)

ret = ret[0]

ret = json.loads(ret)

with open("36kr.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=2))

print(ret)
