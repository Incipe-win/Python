import requests
from lxml import etree
import re


class TiBa:
    def __init__(self, tieba_name):
        self.raw_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
            "cookie": "BAIDUID=C16D9435DA7AC0E9D873752B93EF217D:FG=1; BIDUPSID=C16D9435DA7AC0E9D873752B93EF217D; PSTM=1589699760; delPer=0; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ZD_ENTRY=google; TIEBAUID=cb23caae14130a0d384a57f1; TIEBA_USERTYPE=f26212b2049a7694ade8588c; st_key_id=17; IS_NEW_USER=c85ddd0f5293c36f6910988d; BAIDU_WISE_UID=wapp_1589779587566_657; USER_JUMP=-1; CLIENTHEIGHT=812; CLIENTWIDTH=375; LASW=375; mo_originid=2; SEENKW=%E6%9D%8E%E6%AF%85%23%C0%EE%D2%E3; pb_prompt=1; SET_PB_IMAGE_WIDTH=355; BDRCVFR[crKvfqdHttR]=mbxnW11j9Dfmh7GuZR8mvqV; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1589779555,1589781798,1589782250; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_PSSID=1447_21100_31111_31589_31605_31463_30823_22158; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1589805495; st_data=b09c90a7facf3f770590049edc53d40d92a20ce4735fc4c72cc891f0087ed101a779cd4e7d2df277e764945fad4a381ef6adeddc978bb393f256f481902c28d31761dd980d8d14a4fbecfaa284294800d16579e792d20efb21d979dc8b16d3133a726d9d369c7206c0361323fd3285bfb7970f2e0954ab35e33981a9063bf6f1b162bc12d5967b6ffe87ade6404af348; st_sign=f37770be"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        print(response.status_code)
        return response.content.decode()

    def get_content_list(self, html_str):
        html_str = re.sub(r"<!--", "", html_str)
        html_str = re.sub(r"--\>", "", html_str)
        # self.save_content(html_str)
        html = etree.HTML(html_str)
        content_list = html.xpath(
            "//div[@class=\"threadlist_abs threadlist_abs_onlyline \"]/text()")
        print(content_list)
        img_list = html.xpath(
            "//ul[@class=\"threadlist_media j_threadlist_media clearfix\"]/li/a/img/@src | //ul[@class=\"threadlist_media j_threadlist_media clearfix\"]/li/a/img/@data-original | //ul[@class=\"threadlist_media j_threadlist_media clearfix\"]/li/a/img/@bpic")

    def save_content(self, content):
        with open("html.html", "w", encoding="utf-8") as f:
            f.write(content)

    def run(self):
        pn = 0
        url = self.raw_url.format(pn)
        html_str = self.parse_url(url)
        self.save_content(html_str)
        self.get_content_list(html_str)


if __name__ == "__main__":
    tiba = TiBa("贴吧热议")
    tiba.run()
