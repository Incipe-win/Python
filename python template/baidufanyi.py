import requests
import json
import sys
import execjs


class BaiduFanyi:
    def __init__(self, trans_str):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36",
            "cookie": "BAIDUID=176A5577A3421D782F9762675A710C2C:FG=1; BIDUPSID=176A5577A3421D782F9762675A710C2C; PSTM=1588036939; BDUSS=nNwM3V0N0hvNHhZNm5VcW05dFpzQ2NaTjR1UzBmUjRLNGZrTDVQcHdTSmxYOVplRUFBQUFBJCQAAAAAAAAAAAEAAAC9AFRNaW5jaXBlY2hhbwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGXSrl5l0q5ea; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=146741_142019_146170_145497_144118_147027_145333_147002_147280_146537_131246_144682_137746_144250_146573_146873_127969_146549_145968_146753_145418_146732_145996_131424_146801_114552_142205_146002_107311_147136_147233_146135_139909_146396_144966_145607_139884_144535_145399_143860_146799_139914_110085; delPer=0; PSINO=6; BDRCVFR[5IRyTarJWqT]=mbxnW11j9Dfmh7GuZR8mvqV; ZD_ENTRY=google; session_name=www.google.com; session_id=1589548801428; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1589598746; H_PS_PSSID=31627_1469_31326_21126_31110_31589_31661_31463_31229_30823_22158; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1589598104,1589614835; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1589614842; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1589614842; yjs_js_security_passport=d996c5118806fb7d0978d274e26bf042e6a332c5_1589614815_js"
        }
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.tans_url = "https://fanyi.baidu.com/basetrans"
        with open('baidu_translate_js.js', 'r', encoding='utf-8') as f:
            self.ctx = execjs.compile(f.read())

    def parse_url(self, url, data):
        # print(url)
        response = requests.post(url, data=data, headers=self.headers)
        # print(response.status_code)
        # print(response.content.decode())
        return json.loads(response.content.decode())

    def get_str(sel, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("Translate is: ", ret)

    def get_trans_data(self, lang):
        trans_data = {
            "query": self.trans_str,
            "from": "zh",
            "to": "en",
            "token": "db1b24fa144367386cdc27b5b106eea2",
            "sign": ""
        } if lang == "zh" else {
            "query": self.trans_str,
            "from": "en",
            "to": "zh",
            "token": "db1b24fa144367386cdc27b5b106eea2",
            "sign": ""
        }
        return trans_data

    def exe_js(self):
        sign = self.ctx.call('e', self.trans_str)
        # print(sign)
        return sign

    def run(self):
        lang_detect_data = {"query": self.trans_str}
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]
        trans_data = self.get_trans_data(lang)
        sign = self.exe_js()
        trans_data["sign"] = sign
        # print(trans_data)
        dict_response = self.parse_url(self.tans_url, trans_data)
        self.get_str(dict_response)


if __name__ == "__main__":
    trans_str = sys.argv[1]
    # print(trans_str)
    baidufanyi = BaiduFanyi(trans_str)
    baidufanyi.run()
