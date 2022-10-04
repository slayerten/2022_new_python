import requests


def main():

    url = 'https://cn.bing.com/search?'
    kw = input('Enter a word:')
    params = {'q': kw}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.27'
    }
    reponse = requests.get(url=url, params=params, headers=headers)

    page_text = reponse.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf8') as f:
        f.write(page_text)
    print(fileName, '保存成功!!!')


if __name__ == '__main__':
    main()
