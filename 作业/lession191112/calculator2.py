# coding=utf8
from appium import webdriver
import time, traceback
def Btn_click(textnum):
    driver.find_element_by_xpath(textnum).click()
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'test'
# desired_caps['app'] = r'g:\apk\com.ibox.calculators_3.1.0_1310.apk'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity'] = 'com.ibox.calculators.SplashActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000
# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    driver.implicitly_wait(10)
    Btn_click("//*[@text='C']")
    time.sleep(1)
    Btn_click("//*[@text='3']")
    Btn_click("//*[@text='+']")
    Btn_click("//*[@text='9']")
    Btn_click("//*[@text='=']")
    time.sleep(1)
    Btn_click("//*[@text='×']")
    Btn_click("//*[@text='5']")
    Btn_click("//*[@text='=']")
    time.sleep(1)
    result=driver.find_element_by_xpath("//android.widget.RelativeLayout/android.widget.TextView[2]").text
    print(result)
    if result=='60':
        print("测试通过")
    else:
        print("测试不通过")
    pass
except:
    print(traceback.format_exc())
input('**** Press to quit..')
driver.quit()

