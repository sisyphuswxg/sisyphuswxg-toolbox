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
        if "photo" in str(picture):
            yield picture.get("src")


def download_pic(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ' 'Win64; x64) ' 'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/86.0.4240.111 Safari/537.36 '
    }
    resp = requests.get(url, headers=headers)
    tmp_name = url.split('/')[-1].split('.')[0]
    with open(f"img_{tmp_name}.jpg", "wb") as f:
        f.write(resp.content)


def main(offset):
    url = "https://www.douban.com/photos/album/1882740187/?m_start=" + str(offset)
    print("url: ", url)
    html = get_one_page(url)
    for one_url in parse_one_page(html):
        print(one_url)
        download_pic(one_url)
        time.sleep(3)


if __name__ == "__main__":

    # range(61, 70)     done!
    # range(51, 61)     done!
    # range(41, 51)     done!
    # range(31, 41)     done!
    for i in range(21, 31):
        main(i * 18)
