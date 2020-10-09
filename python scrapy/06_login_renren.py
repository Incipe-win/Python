import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
    "Cookie": "anonymid=ka96pozs-yjimvp; depovince=GW; _r01_=1; JSESSIONID=abcTkH-T9ipJV7hq37Bix; ick_login=ff638c4c-ba6b-40ce-8453-86718f6f2ae7; taihe_bi_sdk_uid=b880e026cd8288adecbb6a5283650383; taihe_bi_sdk_session=4796cf3d9c4b4494745288ec5c64f0fd; loginfrom=null; wp_fold=0; vip=1; t=e2fe6000393188a8e59802b8f74939051; societyguester=e2fe6000393188a8e59802b8f74939051; id=974448101; xnsid=e4059303; jebecookies=be419a6e-b7ba-4f39-9eb1-72442687e78d|||||; ver=7.0"
}

response = requests.get(
    "http://www.renren.com/872201594/profile", headers=headers)

with open("renren1.html", "w", encoding="utf8") as f:
    f.write(response.content.decode())
