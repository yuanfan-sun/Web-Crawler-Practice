import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    # 页码遍历
    page = 1
    while page < 1000:
        page = page + 1
        # 转换页码为string
        converted_page = str(page)
        url = 'https://sc.chinaz.com/jianli/free_' + converted_page + '.html'
        # 请求网址
        page_text = requests.get(url=url, headers=headers).text
        # 实例化
        tree = etree.HTML(page_text)
        resume_url_list = tree.xpath('// *[ @ id = "container"]/div')
        # 建立文件夹
        if not os.path.exists('./resume'):
            os.mkdir('./resume')
        for resume in resume_url_list:
            # 获取一页的下载地址
            resume_url_site = 'https:' + resume.xpath('./a/@href')[0]
            # 获取下载页响应
            downloadPage_text = requests.get(url=resume_url_site, headers=headers).text
            # 实例化新网址
            new_tree = etree.HTML(downloadPage_text)
            resume_lists = new_tree.xpath('//div[@class="ppt_tit clearfix"]')
            for resume_url in resume_lists:
                # 获取简历模板名称
                resume_name = resume_url.xpath('./h1/text()')[0]
                resume_name = resume_name.encode('iso-8859-1').decode('utf-8') + '.rar'
                # 获取简历模板下载地址
                resume_download = resume_url.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
                # 请求简历模板进行持久化存储
                resume_data = requests.get(url=resume_download, headers=headers).content
                resume_path = 'resume/' + resume_name
                with open(resume_path, 'wb') as fp:
                    fp.write(resume_data)
                    print(resume_name, '下载成功！！！')
            fp.close()

