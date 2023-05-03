import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li')
    all_city_names = []
    for li in li_list:
        city_name_list = li.xpath('./a/text()')[0]
        all_city_names.append(city_name_list)
    print(all_city_names, len(all_city_names))
# 在xpath(|) 两边的都可以得到