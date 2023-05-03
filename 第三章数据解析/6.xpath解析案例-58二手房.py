import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    url = 'https://www.58.com/ppkchuzu671/index.html/'

    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    li_list = tree.xpath('//ul[@class="list"]/li')
    fp = open('58.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.xpath('./a/div[2]/p/text()')[0]
        print(title)
        fp.write(title + '\n')
