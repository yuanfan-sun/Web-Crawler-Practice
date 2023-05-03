import requests
if __name__ == "__main__":
    # step_1:指定url
    url = 'https://www.sogou.com'
    # step_2:发起请求
    response = requests.get(url=url)
    # step_3:获取响应数据。text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)
    # step_4: 持久化存储
    with open('./sougou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('finish')
