
import json
import requests


def main():
    url = 'https://movie.douban.com/j/chart/top_list?'
    # 'type=3&interval_id=100:90&action=&start=0&limit=1'
    # type_name=犯罪&type=3&interval_id=100:90&action=
    params = {
        # 'type_name': '犯罪',
        'type': '14',
        'interval_id': '100: 90',
        'action': '',
        'start': '40',
        'limit': '20'

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url, params=params, headers=headers)
    list_data = response.json()
    print(list_data)
    fp = open('./douba5n.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('Over!')


if __name__ == '__main__':
    main()
