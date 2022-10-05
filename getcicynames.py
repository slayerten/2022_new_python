from wsgiref import headers
import requests
from lxml import etree

if __name__ == '__main__':

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    response = requests.get(url, headers)
    page_text = response.text
    print(page_text)
    tree = etree.HTML(page_text)
    all_li_names = tree.xpath('//li')
    for name in all_li_names:
        all_city_name = name.xpath('./a/text()')[0]
        print(all_city_name)
