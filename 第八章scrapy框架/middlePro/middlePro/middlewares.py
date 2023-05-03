# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapy.http import HtmlResponse
from time import sleep


class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    user_agent_list = ['', '']
    PROXY_http = ['', '']
    PROXY_https = ['', '']

    # 拦截请求
    def process_request(self, request, spider):
        # UA伪装
        request.headers['User-Agent'] = random.choice(self.user_agent_list)
        return None

    # 拦截所有响应
    def process_response(self, request, response, spider):  # spider表示爬虫对象
        browser = spider.browser  # 获取了在爬虫类中定义的浏览器对象

        if request.url in spider.models_urls:
            browser.get(request.url)  # 板块对应的url进行请求发送
            sleep(2)
            page_text = browser.page_source  # 包含了动态加载了的新闻

            # response # 板块对应的响应对象
            # 针对定位到的这些response进行篡改
            # 实例化一个新的响应对象（符合需求：包含动态加载出的新闻数据），替代旧的响应对象
            # 如何获取动态加载出的新闻数据？
                # 基于selenium便捷地获取动态加载数据
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)

            return new_response
        else:
            # response # 其他请求对应的响应对象
            return response

    # 拦截发生异常的请求
    def process_exception(self, request, exception, spider):
        if request.url.split(':')[0] == 'http':
            # 代理
            request.meta['proxy'] = 'http://' + random.choice(self.PROXY_http)
        else:
            request.meta['proxy'] = 'https://' + random.choice(self.PROXY_https)

        return request  # 将休整之后的请求对象进行重新的请求发送
