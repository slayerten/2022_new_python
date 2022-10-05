from genericpath import exists
import requests
import os
from bs4 import BeautifulSoup


def main():

    def get_response_text(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers)
        return response.text

    def get_text_down():
        if not os.path.exists('./sanguo'):
            os.mkdir('./sanguo')
        for i in range(7493, 7613):
            # for i in range(7493, 7495):
            url = f'http://guoxue.lishichunqiu.com/gdxs/sanguoyanyi/{i}.html'
            soup = BeautifulSoup(get_response_text(url), 'lxml')
            title = soup.select('#maincontent > h2')[0].text
            content = soup.select('#content ')[0].text
            text_name = './sanguo/'+str(i-7492)+'.text'
            with open(text_name, 'w', encoding='utf-8') as fp:
                fp.write(title)
                fp.write(content)

    get_text_down()


if __name__ == '__main__':
    main()
