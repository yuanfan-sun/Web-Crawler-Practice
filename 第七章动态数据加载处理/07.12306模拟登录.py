from selenium import webdriver
import time
from PIL import Image

path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(1)

browser.save_screenshot('12306.png')

code_img_ele = browser.find_element_by_xpath('')
location = code_img_ele.location
size = code_img_ele.size
rangle = (
    int(location['x']), int(location['y']), int(location(['x']) + size['width']), int(location(['y']) + size['height']))

i = Image.open('./2306.png')
code_img_name = './code.png'
frame = i.crop(rangle)
frame.save(code_img_name)
