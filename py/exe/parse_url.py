import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}
# proxies = dict(http='socks5://127.0.0.1:7891',
# https='socks5://127.0.0.1:7891')
proxies = dict()


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):
    print("*" * 20)
    if method == "POST":
        response = requests.post(
            url, data=data, headers=headers, timeout=3, proxies=proxies)
    else:
        response = requests.get(url, headers=headers,
                                timeout=3, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


# if __name__ == "__main__":
#     url = "https://www.google.com/"
#     with open("test.html", "w", encoding="utf-8") as f:
#         f.write(parse_url(url, proxies))
