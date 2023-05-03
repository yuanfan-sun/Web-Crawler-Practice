import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    if not os.path.exists('./wallheaven'):
        os.mkdir('./wallheaven')
    page = 0
    while page < 10:
        page = page + 1
        # 转换页码为string
        converted_page = str(page)
        url = 'https://wallhaven.cc/toplist?page=' + converted_page
        # 请求网址
        page_text = requests.get(url=url, headers=headers).text
        # 实例化
        tree = etree.HTML(page_text)
        a_list = tree.xpath('//a[@class="preview"]')
        for a in a_list:
            img_href = a.xpath('./@href')[0]
            img_text = requests.get(url=img_href, headers=headers).text
            # 实例化
            new_tree = etree.HTML(img_text)
            img_list = new_tree.xpath('//img[@id="wallpaper"]')
            for img in img_list:
                img_src = img.xpath('./@src')[0]
                img_data = requests.get(url=img_src, headers=headers).content
                img_id = img.xpath('./@data-wallpaper-id')[0]
                img_name = img_id + '.jpg'
                img_path = 'wallheaven/' + img_name
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                    print(img_name, '下载成功！！！')
            fp.close()
