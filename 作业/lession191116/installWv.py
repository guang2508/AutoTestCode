# coding=utf8
from appium import webdriver
# from selenium import webdriver
import time, traceback
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
desired_caps['app'] = r'g:\apk\wv.apk'
# desired_caps['appPackage'] = 'com.example.jcy.wvtest'
# desired_caps['appActivity'] = 'com.example.jcy.wvtest.MainActivity'
# desired_caps['browerName'] = 'Chrome'
# desired_caps['chromedriverExecutableDir'] = r'D:\webdrivers\v76'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    # #1、打开电脑上的浏览器以手机模式运行
    # chrome_options=webdriver.ChromeOptions()
    # #2、选择一种存在的模拟手机设备类型
    # chrome_options.add_experimental_option("mobileEmulation",{"deviceName":"iphone X"})
    # #3、添加配置
    # driver=webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())
    driver.implicitly_wait(10)
    # driver.get('http://www.baidu.com')
    time.sleep(2)
    # print(driver.current_context)
    # print(driver.contexts)
    if driver.current_context!='NATIVE_APP':#判断是否原生
        driver.switch_to.context('NATIVE_APP')
    ele=driver.find_element_by_xpath('//*[@resource-id="index-kw"]').send_keys('松勤\n')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@resource-id="index-bn"]').click()
    # print(driver.current_context)
    # ele.send_keys('松勤\n')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@content-desc="通知"]').click()
    pass
except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()

