import requests
from lxml import etree
import os

if __name__ == '__main__':
    '''
    login_url = 'https://wallhaven.cc/login'
     data = {
        '_token': 'FS78RoT67lQxbCtfZFhWfzlo3o5fMQrCzE60w0FH',
        'username': 'franksun98',
        'password': 'Syf980212720120'
    }
    session = requests.Session()
    # 使用session进行post请求发送
    response = session.post(url=login_url, headers=headers, data=data)
    print(response.status_code)
    login_page_text = response.text
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Cookie': '_pk_id.1.01b8=1cbdc864aba5d2a8.1606129475.; __cfduid=dacc7cee5711eb37e36c403af97dfffbe1617544730; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InhSZlUrSXRPeE9oRjV1RkxKN3ZFQXc9PSIsInZhbHVlIjoiSldLZzRxOWZMYVdxVU10S0ZBcUpKVG8yMDBTekRIUjNkTzRWZTdBazNrc1Q4SUtqdkxPOE5vTEhuWWwrMklSXC8yVzduclYwZ2dWNFVjcVhwbDJNdDNPSWJEVWhkQlBsOHFMVTBhZ1BITkhwUTdYYXFqbG00NkxXSG5cL2lSRCs5WFc4YlIwYW12SG1wSThDWWx6aEdDZmRYa2lSSjNcLzhjQ1NpanVvUlBIWlNmandpeUNzejlYTjluSXNUK1wvVTVRZyIsIm1hYyI6IjRlNGI0NDAxZmU5OTk4YTYyZmUyYzIyZDE0YjU1MzIzNzhhZDI3YmNkNjFmYjZiYmY4Y2U0MjhhY2RlMWRhZjAifQ%3D%3D; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkV1VytSbXk0RjhBQnBEU3JQTlRLRlE9PSIsInZhbHVlIjoiMGt6aVpVQnhBdHZCaDNwQStFUDU4NzJtekpPTnRuZkRZMzhlOWllb1M5WlZFVWY0ck5YQ0I5MWFVellyTGI3USIsIm1hYyI6ImE3ZTVmNmMzMDJmNGI5YTQ0MTFjNTNhZDZkOTRiYTc0NTEyMWRlMjhlNTQ5ZmJkMDM0YzcwZWZiNjYzZWNkMjcifQ%3D%3D; wallhaven_session=eyJpdiI6InJmY2hFbWNENzVuWGRWcGxIcHRORnc9PSIsInZhbHVlIjoiQXRBTWFUSGN6UXJNZGRCazhcL0ZsWGZGeUdLK0czK0FXdHVKNEpjUVp5cEZZc1pIUTFkUUpVR3JZOGRBeG9rRVkiLCJtYWMiOiIwNTdiZjBmYWFiNzI1NmQ4NjkxYmQxODU1ODg5YzkwNDVjOTk3NDFhMzQzZTFjMmEwOGI0OGFjMDliY2E4ODFlIn0%3D'
    }
    if not os.path.exists('D:/学习/web crawler/wallheavenNSFW'):
        os.mkdir('D:/学习/web crawler/wallheavenNSFW')

    for page in range(10):
        # 转换页码为string
        converted_page = str(page)
        url = 'https://wallhaven.cc/search?categories=111&purity=001&topRange=1M&sorting=toplist&order=desc&page=' + converted_page
        # 请求网址 使用携带cookie的session进行get请求 #requests改成session
        page_text = requests.get(url=url, headers=headers).text
        print(page_text)
        # 实例化
        tree = etree.HTML(page_text)
        a_list = tree.xpath('//*[@id="thumbs"]/section/ul/li[1]/figure/a[2]')
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
                img_path = 'D:/学习/web crawler/wallheavenNSFW/' + img_name
                with open(img_path, 'wb') as fp:
                    fp.write(img_data)
                    print(img_name, '下载成功！！！')
            fp.close()
