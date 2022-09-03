#!/usr/bin/python
# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-10
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
#连接设备
device=MonkeyRunner.waitForConnection(3,"127.0.0.1:62001")
#启动APP
device.startActivity("com.UCMobile.x86/com.uc.browser.InnerUCMobile")
#等待2s
MonkeyRunner.sleep(2)
#点击搜索框
device.touch(500,250,"DOWN_AND_UP")
MonkeyRunner.sleep(1)
#输入查询词
device.type("test")
MonkeyRunner.sleep(1)
#点击回车键进行搜索
device.press('KEYCODE_ENTER','DOWN_AND_UP')
MonkeyRunner.sleep(6)
#截图
image=device.takeSnapshot()
image.writeToFile('./test.png','png')

