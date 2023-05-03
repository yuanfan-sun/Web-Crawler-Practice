import requests
import json

if __name__ == '__main__':
    # 1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    # 3.post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw': word
    }
    # 4.请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据：jason方法返回的是obj(如果确认响应数据是jason类型的，才可以用jason)
    dict_obj = response.json()
    # 6.持久化存储
    filename = word+'.json'
    fp = open(filename, 'w', encoding='utf-8')
    json.dump(dict_obj, fp=fp, ensure_ascii=False)

    print('over!!!')