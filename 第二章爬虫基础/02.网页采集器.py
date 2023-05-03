# UA：user-agent
# UA检测：门户网站会检查对应请求的身份标识，简单来说就是检测你是不是人，如果UA是某一款浏览器，就确定你是个正常用户，以爬虫请求则可能被拒绝
# UA伪装：让爬虫对应的请求载体身份标识（UA）伪装成浏览器
import requests
if __name__ == "__main__":
    # UA伪装：将对应的UA封装到字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数:封装到字典中
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    page_text = response.text
    filename = kw+'.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print(filename, '保存成功！！！')

