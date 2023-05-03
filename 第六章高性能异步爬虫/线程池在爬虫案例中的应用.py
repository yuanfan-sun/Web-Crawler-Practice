import requests
import random
from lxml import etree
import re
import json
from multiprocessing.dummy import Pool
import os

if not os.path.exists('./lishiping'):
    os.mkdir('./lishiping')
url = 'https://www.pearvideo.com/popular_59'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
}
# 请求网页
page_text = requests.get(url=url, headers=headers).text
# 实例化
tree = etree.HTML(page_text)
video_list = tree.xpath('//*[@id="popularList"]/li/div[2]/a')
# 建立urls字典
urls = []
for video in video_list:
    video_url_part = video.xpath('./@href')[0]
    video_page_url = 'https://www.pearvideo.com/' + video_url_part
    video_name = video.xpath('./h2/text()')[0] + '.mp4'
    video_page_text = requests.get(url=video_page_url, headers=headers).text
    # 从详情页中解析视频地址
    headers_json = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Referer': video_page_url
    }
    contId = video_url_part.split('_')[1]
    param = {
        'contId': contId,
        'mrd': str(random.random())
    }
    jsonResponse_url = 'https://www.pearvideo.com/videoStatus.jsp'
    response = requests.get(url=jsonResponse_url, params=param, headers=headers_json)
    data = response.json()
    s = json.dumps(data)
    # print(s)
    ex = 'srcUrl": "(.*?)"}}}'
    video_fake_url = re.findall(ex, s)[0]  # https://video.pearvideo.com/mp4/third/20210329/1617645588212-12719568-190144-hd.mp4
    head_url = video_fake_url[0:47]
    ass_url = 'cont-' + contId + video_fake_url[-23:]
    real_url = head_url + ass_url  # https://video.pearvideo.com/mp4/third/20210329/cont-1724902-12719568-190144-hd.mp4

    dic = {
        'name': video_name,
        'url': real_url
    }
    urls.append(dic)

def get_video_data(dic):
    url = dic['url']
    print(dic['name'], '正在下载...')
    video_data = requests.get(url=url, headers=headers).content
    # 持久化存储
    with open('lishiping/'+dic['name'], 'wb', ) as fp:
        fp.write(video_data)
        print(dic['name'], '下载成功！')


pool = Pool(len(dic))
pool.map(get_video_data, urls)

pool.close()
# 主线程结束之后子线程再结束
pool.join()
