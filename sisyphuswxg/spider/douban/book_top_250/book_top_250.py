# encoding: utf-8


import re
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import csv


def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; ' 'Win64; x64) ' 'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/86.0.4240.111 Safari/537.36 '
        }
        resp = requests.get(url, headers=headers)
        print(resp)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    tables = soup.findAll('table', {'width': '100%'})
    for table in tables:
        # 书名
        name = table.div.a.text
        name = name.replace('\n', '').replace(' ', '')  # 处理多余字符
        # 别名
        alias = table.div.span
        # 无别名的使用书名代替
        if alias:
            alias = alias.text
        else:
            alias = name
        # url
        url = table.div.a['href']
        # 信息
        info = table.find('p', {'class': 'pl'})
        info = info.text.strip()
        # 评分
        score = table.find('span', {'class': 'rating_nums'})
        score = score.text
        # 评分人数
        rating_num = table.find('span', {'class': 'pl'})
        rating_num = rating_num.text.strip()
        rating_num = re.findall('(\d+)人评价', rating_num)[0]
        # 描述
        desc = table.find('p', {'class': 'quote'})
        # 存在书的描述为空，做处理：
        if desc:
            desc = desc.text.strip()
        else:
            desc = ""
        yield {
            'name': name,
            'alias': alias,
            'url': url,
            'info': info,
            'score': score,
            'rating_num': rating_num,
            'desc': desc
        }


def write_header():
    with open('book_top_250.csv', mode='a', newline='', encoding='utf-8-sig') as csvfile: # mode='a' 表示追加
        writer = csv.writer(csvfile)
        header = ['书名', '别名', '链接', '信息', '评分', '评分人数', '描述']
        writer.writerow(header)


def write_to_file(book):
    with open('book_top_250.csv', mode='a', newline='', encoding='utf-8-sig') as csvfile: # mode='a' 表示追加
        writer = csv.writer(csvfile)
        writer.writerow([book['name'], book['alias'], book['url'], book['info'], book['score'], book['rating_num'], book['desc']])


def main(offset):
    url = "https://book.douban.com/top250?start=" + str(offset)
    html = get_one_page(url)
    print("html: ", html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    # 表的第一行 -> 列名
    write_header()

    for i in range(10):
        main(i * 25)
