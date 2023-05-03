from selenium import webdriver
from time import sleep
# 导入动作链对应的类
from selenium.webdriver import ActionChains

path = r'D:\学习\web crawler\第七章动态数据加载处理\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 如果定位的标签是存在于iframe标签之中的，则必须通过如下操作再进行标签定位
browser.switch_to.frame('iframeResult')  # 切换浏览器标签定位的作用域-
div = browser.find_element_by_xpath('//div[@id="draggable"]')

# 动作链(连续的动作)
action = ActionChains(browser)
# 点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    # perform()立即执行动作链操作
    # move_by_offset(x, y) 两个方向
    action.move_by_offset(17, 0).perform()
    sleep(0.3)

# 释放动作链
action.release()
browser.quit()