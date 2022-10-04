
import requests
from lxml import etree
import re

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'https://wallspic.com/cn/album/3840x2160'
    page_text = requests.get(url=url, headers=headers).text

    print(page_text
          )
    tree = etree.HTML(page_text)
    # print(tree)
    url_list = tree.xpath(
        '//div[@class="gallery_fluid"]/div[@class="gallery_fluid-column"]/a')
    print(url_list
          )
    for url in url_list:
        print(url)
        # pic_data = requests.get(url, headers).content
        # with open('hill.jpg', 'wb') as fb:
        #     fb.write(pic_data)
        #     print('pic is downloaded.')
