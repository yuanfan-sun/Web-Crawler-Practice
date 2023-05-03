import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
page_text = requests.get(url='http://www.baidu.com/s?wd=ip', headers=headers, proxies={"https": '106.75.226.36'}).text
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
