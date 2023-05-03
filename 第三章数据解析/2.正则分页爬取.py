import requests
import re
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    # 创建一个文件夹，保存所有图片
    if not os.path.exists('./qiutuLibs'):
        os.makedirs('./qiutuLibs')
    # 设置通用url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'

    for pageNum in range(1, 36):
        # 对应页码的url
        new_url = format(url%pageNum)

        page_text = requests.get(url=new_url, headers=headers).text

        # 聚焦爬虫将图片地址进行提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        # print(img_src_list)
        for src in img_src_list:
            # 拼接出完整url
            src = 'https:' + src
            # 请求到图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储的路径
            imgPath = './qiutuLibs/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功！！')
