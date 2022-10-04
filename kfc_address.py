import json
from urllib import response
import requests


def main():

    url = 'http: // www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op = cname'
    keyword = input('Enter a keyword')
    params = {
        'op': 'cname',
        'cname': '',
        'pid': '',

        'keyword': op
        'pageIndex': '1',
        'pageSize': '10'

    }


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
response = requests.post(url=url, params=params, headers=headers)

if __name__ == '__main__':
    main()
