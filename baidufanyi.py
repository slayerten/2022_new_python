from email import header
import requests
import json


def main():

    post_url = "https://fanyi.baidu.com/sug"

    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.33'
    }
    keyword = input('Enter a word:')
    data = {'kw': keyword}

    response = requests.post(url=post_url, data=data, headers=header)
    dict_obj = response.json()
    # print(dict_obj)

    filename = keyword + '.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False)


if __name__ == "__main__":
    main()
