# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-01
import threading
import requests
res = ''
url1=r'http://mirrors.163.com/centos/6/isos/x86_64/README.txt'
url2=r'http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt'
l=threading.Lock()
# def getWebText(url):
#     # 声明使用全局变量
#     global res
#     res = requests.get(url).text+res
# with open('G:\\readme89.txt','w+') as f:
#     t1 = Thread(target=getWebText, args=(url1,))
#     t2 = Thread(target=getWebText, args=(url2,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     f.write(res)

def getWebText(url):
    # 声明使用全局变量
    global res
    l.acquire()
    res = requests.get(url).text
    with open('G:\\readme89.txt','a') as f:
        f.write(res)
    l.release()
t1 = threading.Thread(target=getWebText, args=(url1,))
t2 = threading.Thread(target=getWebText, args=(url2,))
t1.start()
t2.start()
t1.join()
t2.join()

