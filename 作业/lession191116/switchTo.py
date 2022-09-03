# coding=utf8
from appium import webdriver
import time, traceback
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'g:\apk\toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@class="android.support.v7.app.ActionBar$Tab"][1]').click()
    time.sleep(1)
    title1=driver.find_element_by_id("io.manong.developerdaily:id/tv_title").text
    ele=driver.find_element_by_id("io.manong.developerdaily:id/tv_title")#此处默认选择第一篇
    ele.click()
    time.sleep(1)
    title2=driver.find_element_by_xpath('//*[@resource-id	="io.manong.developerdaily:id/header_view"]/*[1]').text
    if title1==title2:
        print('能正常打开第一篇文章')
    else:
        print('不能正常打开第一篇文章')
        driver.quit()
    driver.find_element_by_xpath('//*[@resource-id="io.manong.developerdaily:id/toolbar"]/*[@class="android.widget.ImageButton"]').click()#点击返回箭头
    time.sleep(2)
    title3=driver.find_element_by_id("io.manong.developerdaily:id/tv_title").text
    if title3==title1:
        print('能正常返回')
    else:
        print('不能正常返回')
        driver.quit()
    pass
except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()

