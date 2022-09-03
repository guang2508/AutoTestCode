# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
import random,time
class tiger():
    def __init__(self,inweight=200):
        self.weight=inweight
        # print(self.weight)

    def food(self,feed):
        while True:
            if feed=='meat':
                self.weight += 10
                print(self.weight)
                break
            elif feed=='grass':
                self.weight -= 10
                print(self.weight)
                break
            else:
                feed=input('输入不正确，请重新选择食物,meat or grass')

    def knock(self):
        print('~~~~~~wow')
        self.weight -= 5
        print(self.weight)

class sheep():
    def __init__(self,inweight=100):
        self.weight=inweight
        # print(self.weight)

    def food(self,feed):
        while True:
            if feed=='grass':
                self.weight += 10
                print(self.weight)
                break
            elif feed=='meat':
                self.weight -= 10
                print(self.weight)
                break
            else:
                feed=input('输入不正确，请重新选择食物，meat or grass')

    def knock(self):
        print('~~~~~~mee')
        self.weight -= 5
        print(self.weight)

class room():
    roomlist=['']*10
    for i in range(0,10):
        if random.randint(0,1)==0:
            roomlist[i]=tiger()
        else:
            roomlist[i]=sheep()

timeStart=time.time()
gameInit=room()
while True:
    roomId=random.randint(1,10)
    sel=input(f'现在为{roomId}号房间,请选择1、喂食，2、敲门')
    while True:
        if sel=='1':
            feed=input('请选择食物，meat or grass')
            gameInit.roomlist[roomId-1].food(feed)
            break
        elif sel=='2':
            gameInit.roomlist[roomId-1].knock()
            break
        else:
            print(f'您的输入有误，现在为{roomId}号房间,请选择1、喂食，2、敲门')
    timeEnd=time.time()
    if (timeEnd-timeStart)>30:
        print('游戏结束')
        for i in range(1,11):
            print(i,gameInit.roomlist[i - 1].weight)
        break


