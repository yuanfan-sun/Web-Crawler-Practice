import requests

if __name__ == '__main__':
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    word = input('enter a word:')
    data = {
        'cname': '',
        'pid': '',
        'keyword': word,
        'pageIndex': 1,
        'pagesize': '10',
        'op': 'keyword'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
# 记得post请求不用get用post
    response = requests.post(url=post_url, data=data, headers=headers)
    page_text = response.text
    filename = str(word) + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('over!!!')
