#-*- coding: utf-8 -*-
#@File    : handle_mock.py
#@Time    : 2021/11/22 20:36
#@Author  : xintian
#@Email   : 1730588479@qq.com
#@Software: PyCharm
#Date:2021/11/22
import requests
import time
import threading#多线程模块
HOST = 'http://127.0.0.1:9999'
# def test():
#     payload = {"key1":"abc","key2":"123"}
#     resp = requests.get(url=f'{HOST}/xt',json=payload)
#     print(resp.text)
#
# if __name__ == '__main__':
#     test()

#----------提交申请
def commit_order(inData):
    url = f'{HOST}/api/order/create/'
    payload = inData
    resp = requests.post(url,json=payload)
    return resp.json()


#--------------查询接口-------------------
"""
查询接口注意事项：
    1- 使用什么去查询--id
    2- 频率 interval
    3- 没有查询到，多久认为是超时 timeout
"""
def get_order_result(orderID,interval=5,timeout=30):
    """
    :param orderID: 申请id
    :param interval: 频率
    :param timeout: 超时时间
    :return: 查询结果
    """
    url = f'{HOST}/api/order/get_result01/'
    payload = {'order_id': orderID}
    #1-记录函数开始运行的时间
    startTime = time.time()#秒数  1970开始算的
    #2- 查询的结束时间
    endTime = startTime + timeout
    #3- 在时间内去查询结果
    cnt = 1#查询次数
    while time.time()<endTime:#当前时间<结束时间
        resp = requests.get(url,params=payload)

        #如果查到结果就退出查询
        if resp.text:
            print(f'第{cnt}次查询，已有结果，停止查询！',resp.text)
            break
        else:
            print(f'第{cnt}次查询，没有查询结果，请等待！')
        time.sleep(interval)
        cnt +=1
    print('---查询操作结束---')



#------------------------------------------------
if __name__ == '__main__':
    startTime = time.time()
    testData = {
        "user_id": "sq123456",
        "goods_id": "20200815",
        "num": 1,
        "amount": 200.6
        }

    res = commit_order(testData)
    orderID = res['order_id']
    print(orderID)

    #-----------------子线程-------------------
    """
    子线程对象 = threading.Thread(target,args)
    target:你把哪一个函数当成子线程，直接传递函数名
    args：你传递的函数需要使用的变量 ---元组类型
    """
    t1 = threading.Thread(target=get_order_result,args=(orderID,))

    # threadList = []
    # for one in range(10):
    #     threadList.append(threading.Thread(target=get_order_result,args=(orderID,)))

    #如果主线程结束，或异常退出，子线程就直接强制结束！
    t1.setDaemon(True)
    t1.start()#开启子线程



    #--------------------------------------------


    #-----自动化执行其他接口代码--------
    for one in range(20):
        time.sleep(1)#自动化发送请求的时间---模拟
        print(f'{one}-我正在执行其他接口的自动化测试')

    endTime = time.time()
    print('整个自动化测试运行耗时>>> ',endTime-startTime)

"""
写代码的流程：功能---性能(效率)优化
问题：
    1- 领导看了你的自动化完成情况，表现出认可，但是是否可以提供执行效率！
分析：
    1- 领导看到是一个现象
    2- 慢的原因：time.sleep(5)
    3- 给方案：
        1- request.xx()和time.sleep()  io阻塞
        2- 效率方案：多进程、多线程、多协程-----比较优化方案：多进程+多协程
            把cpu每一核用上---多进程
            把cpu的每一核用好--多协程
        3- 实现方案：
            1- 主线程是 ----main自动化代码
            2- 子线程---get_order_result





"""
