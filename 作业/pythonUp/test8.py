# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-07
import threading
import requests

def subThread():
    def getWebText(url):
        ret = requests.get(url).text
        return ret
    return getWebText

url1=r'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
url2=r'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
@subThread
t1=threading.Thread(target=getWebText,args=url1)
t2=threading.Thread(target=getWebText,args=url2)
t1.start()
t2.start()
r1=t1.join()
r2=t2.join()
print(r1)

