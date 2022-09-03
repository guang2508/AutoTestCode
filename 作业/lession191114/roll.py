# coding=utf8
from appium import webdriver
import time, traceback
def Btn_click(textnum):
    driver.find_element_by_xpath(textnum).click()
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'g:\apk\sqauto.apk'
desired_caps['appPackage'] = 'com.sqauto'
desired_caps['appActivity'] = 'com.sqauto.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    driver.implicitly_wait(10)
    time.sleep(1)
    lo=driver.get_window_size()
    x1=lo['width']*0.5
    y1=lo['height']*0.8
    y2=lo['height']*0.3
    for i in range(0,3):
        driver.swipe(x1,y1,x1,y2,duration=2000)
        time.sleep(0.5)
    # best=driver.find_element_by_android_uiautomator('new UiSelector().text("口碑最佳")')
    best=driver.find_elements_by_xpath('//*[@text="口碑最佳"]/following-sibling::android.widget.TextView')
    for i in range(0,10,2):
        print(best[i].text)
    # bestIndex=best.index
    # print(best)
except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()

