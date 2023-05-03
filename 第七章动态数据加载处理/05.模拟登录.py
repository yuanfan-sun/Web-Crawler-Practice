from selenium import webdriver
from time import sleep

path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://pixiv.net')