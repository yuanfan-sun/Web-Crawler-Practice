from selenium import webdriver
from lxml import etree
from time import sleep

# 实例化一个浏览器对象(传入浏览器的驱动程序)
path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
#
browser.get('http://scxk.nmpa.gov.cn:81/xk/')

# page_source获取浏览器当前页面的页面源码数据
page_text = browser.page_source

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name = li.xpath('./dl/@title')[0]
    print(name)
sleep(5)
browser.quit()
