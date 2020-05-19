import requests
import json
from parse_url import parse_url
from pprint import pprint

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
html_str = parse_url(url)

ret1 = json.loads(html_str)
pprint(ret1)
print(type(ret1))

with open("douban.json", "w", encoding="utf8") as f:
    f.write(json.dumps(ret1, ensure_ascii=False, indent=2))
