from sqlite3 import paramstyle
import requests


def main():

    url = 'https://www.sogou.com'
    response = requests.get(url)
    page_text = response.text
    print(page_text)
    with open('./sogou.html', 'w', encoding='utf-8') as f:
        f.write(page_text)


if __name__ == "__main__":
    main()
params
