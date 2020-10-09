import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0 Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}


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
    return response.content


def parse_url(url, method="GET", data=None, proxies={}):
    try:
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None
    return html_str


# if __name__ == "__main__":
#     url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0"
#     print(parse_url(url))
