import scrapy
from selenium import webdriver

class XxxSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['xxx.com']
    start_urls = ['http://xxx.com/']
    models_urls = []

    # 实例化一个浏览器对象
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path='')

    def parse(self, response):
        pass
