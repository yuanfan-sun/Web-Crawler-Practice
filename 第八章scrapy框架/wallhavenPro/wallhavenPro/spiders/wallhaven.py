import scrapy
from wallhavenPro.items import WallhavenproItem

class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    # allowed_domains = ['www.wallhaven.com']
    start_urls = []
    set_url = input('添加一个url: ')
    urls = [set_url]
    for url in urls:
        url = str(url)[:-1]+'%d'
        start_urls.append(url)

    page_num = 1

    def start_requests(self):
        cookies = '_pk_id.1.01b8=1cbdc864aba5d2a8.1606129475.; __cfduid=dacc7cee5711eb37e36c403af97dfffbe1617544730; remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6InhSZlUrSXRPeE9oRjV1RkxKN3ZFQXc9PSIsInZhbHVlIjoiSldLZzRxOWZMYVdxVU10S0ZBcUpKVG8yMDBTekRIUjNkTzRWZTdBazNrc1Q4SUtqdkxPOE5vTEhuWWwrMklSXC8yVzduclYwZ2dWNFVjcVhwbDJNdDNPSWJEVWhkQlBsOHFMVTBhZ1BITkhwUTdYYXFqbG00NkxXSG5cL2lSRCs5WFc4YlIwYW12SG1wSThDWWx6aEdDZmRYa2lSSjNcLzhjQ1NpanVvUlBIWlNmandpeUNzejlYTjluSXNUK1wvVTVRZyIsIm1hYyI6IjRlNGI0NDAxZmU5OTk4YTYyZmUyYzIyZDE0YjU1MzIzNzhhZDI3YmNkNjFmYjZiYmY4Y2U0MjhhY2RlMWRhZjAifQ%3D%3D; _pk_ses.1.01b8=1; XSRF-TOKEN=eyJpdiI6IkV1VytSbXk0RjhBQnBEU3JQTlRLRlE9PSIsInZhbHVlIjoiMGt6aVpVQnhBdHZCaDNwQStFUDU4NzJtekpPTnRuZkRZMzhlOWllb1M5WlZFVWY0ck5YQ0I5MWFVellyTGI3USIsIm1hYyI6ImE3ZTVmNmMzMDJmNGI5YTQ0MTFjNTNhZDZkOTRiYTc0NTEyMWRlMjhlNTQ5ZmJkMDM0YzcwZWZiNjYzZWNkMjcifQ%3D%3D; wallhaven_session=eyJpdiI6InJmY2hFbWNENzVuWGRWcGxIcHRORnc9PSIsInZhbHVlIjoiQXRBTWFUSGN6UXJNZGRCazhcL0ZsWGZGeUdLK0czK0FXdHVKNEpjUVp5cEZZc1pIUTFkUUpVR3JZOGRBeG9rRVkiLCJtYWMiOiIwNTdiZjBmYWFiNzI1NmQ4NjkxYmQxODU1ODg5YzkwNDVjOTk3NDFhMzQzZTFjMmEwOGI0OGFjMDliY2E4ODFlIn0%3D'
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, cookies=cookies)

    def parse(self, response):
        li_list = response.xpath('//div[@id="thumbs"]/section/ul/li')
        for li in li_list:
            detail_page_url = li.xpath('./figure/a[2]/@href').extract_first()
            item = WallhavenproItem()
            item['detail_page_url'] = detail_page_url
            yield scrapy.Request(detail_page_url, callback=self.detail_page, meta={'item': item})

    def detail_page(self, response):
        img_list = response.xpath('//img[@id="wallpaper"]')
        for img in img_list:
            item = response.meta['item']
            src = img.xpath('./@src').extract_first()
            item['src'] = src
            yield item
            print(src)
            if self.page_num <= 10:
                for url in self.start_urls:
                    new_url = format(url % self.page_num)
                    self.page_num += 1
                    yield scrapy.Request(url=new_url, callback=self.parse)