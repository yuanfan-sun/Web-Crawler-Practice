import scrapy
from zhipinPro.items import ZhipinproItem

class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c100010000-p100109/?ka=search_100109']

    def parse_detail(self, response):
        item = response.meta['item']
        job_detail = response.xpath('//div[@id="main"]/div[3]/div/div[2]/div[2]/div[1]').extract()
        job_detail = ''.join(job_detail)
        item['job_detail'] = job_detail
        print(job_detail)
        yield item

    def parse(self, response):
        li_list = response.xpath('//div[@id="main"]/div/div[3]/ul')
        for li in li_list:
            job_title = li.xpath('.//div[@class="detail-top-title"]/text()').extract_first()
            job_detail_url = 'https://www.zhipin.com/' + li.xpath('.//div[@class="primary-box"]/@href').extract_first()

            item = ZhipinproItem()
            item['job_title'] = job_title
            print(job_title)
        # 手动请求的发送
        # 请求传参：meta={}可以将meta字典传递给请求对应的回调函数
        yield scrapy.Request(job_detail_url, callback=self.parse_detail, meta={'item': item})
