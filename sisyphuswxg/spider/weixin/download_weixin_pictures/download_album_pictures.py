# encoding: utf-8


from requests.exceptions import RequestException
from bs4 import BeautifulSoup

import requests
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ' 'Win64; x64) ' 'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36 '
        }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            # print("resp text: ", resp.text)
            return resp.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    pictures = soup.find_all(name='img')
    for picture in pictures:
        pic_src = picture.get("data-src")
        if "oeotsl" in str(pic_src):
            # print(pic_src)
            yield pic_src


def download_pic(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ' 'Win64; x64) ' 'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36 '
    }
    resp = requests.get(url, headers=headers)
    tmp_name = url.split('/')[-2][-10:]
    with open(f"img_{tmp_name}.jpg", "wb") as f:
        f.write(resp.content)


def main():
    urls = [
        "https://mp.weixin.qq.com/s/BBQOmBgYd7YHirHKjYNvUg",
        "https://mp.weixin.qq.com/s/5JhddWQwbDoks6MTB0OXiw",
    ]
    # url = "https://mp.weixin.qq.com/s/BW-FdS-WsIv2_YNPle59VA"
    for url in urls:
        html = get_one_page(url)
        for one_url in parse_one_page(html):
            print(one_url)
            download_pic(one_url)
            time.sleep(3)


if __name__ == "__main__":
    main()
