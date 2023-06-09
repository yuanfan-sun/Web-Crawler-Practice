import requests
from bs4 import BeautifulSoup
# import re

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    # 对首页的页面数据进行爬取
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers)
    page_text.encoding = ('utf-8')
    # print(page_text.text)

    # 在首页中解析出章节的标题和详情页的url
    # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text.text, 'lxml')
    # 解析章节和详情页的url
    li_list = soup.select('.book-mulu>ul>li')
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_url, headers=headers)
        detail_page_text.encoding = ('utf-8')
        # re.sub('&nbsp;','',detail_page_text.text)
        detail_soup = BeautifulSoup(detail_page_text.text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节内容
        content = div_tag.text
        fp.write(title + ':' + content + '\n')
        print(title, '爬取成功')