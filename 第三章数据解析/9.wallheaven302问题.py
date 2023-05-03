import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'origin': 'https://wallhaven.cc',
        'referer': 'https://wallhaven.cc/login',
    }

    # 获取token
    login_page_text = requests.get(url='https://wallhaven.cc/login', headers=headers).text
    token_tree = etree.HTML(login_page_text)
    token = token_tree.xpath('//*[@id="login"]/input[1]/@value')[0]
    print(token)

    data = {
        '_token': token,
        'username': 'franksun98',
        'password': 'P9knHZGP7Di@mRW'
    }

    login_response = requests.post(url='https://wallhaven.cc/auth/login', headers=headers, data=data)
    print(login_response.status_code)
