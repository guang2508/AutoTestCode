# author：tang   time:2019-10-22
# 1、建10个房间，每个房间随机放动物。申明房间类、老虎类、羊类。
# 2、随机给出房间号，给与游戏者决策。1、喂食。2、敲门
# 3、时间到则游戏停止
from random import randint  #导入取随机整数模块
import time                 #导入时间模块，用于计时
roomLists=[0]*10            #申明房间列表，为10个空房间
class Tirger:               #申明Tirger类
    name='老虎'
    def __init__(self,weight=200):  #初始化函数，默认Tirger体重为200
        self.tweight=weight
    def roal(self):                 #申明吼叫函数，吼一次减5斤
        self.tweight -= 5
    def food(self,food):            #申明喂食函数，喂肉+10斤，喂草-10斤
        if food=='肉':
            self.tweight += 10
        elif food=='草':
            self.tweight -= 10
    @staticmethod                   #申明静态方法，吼叫（这个貌似可以直接放在吼叫函数内）
    def static_roal():
        print('wow~~')
class Sheep:
    name = '羊'
    def __init__(self, weight=100):
        self.tweight = weight
    def roal(self):
        self.tweight -= 5
    def food(self, food):
        if food == '草':
            self.tweight += 10
        elif food == '肉':
            self.tweight -= 10
    @staticmethod
    def static_roal():
        print('mie~~~')
def AnimalRoom():               #申明方法，给10个房间随机生成动物
    for num in range(0,10):
        if randint(0,1)==1:
            weight = 200
            roomLists[num]=Tirger()
        else:
            weight = 100
            roomLists[num]=Sheep()
startTime=time.time()           #游戏开始时间计时
AnimalRoom()                    #调用方法，每个房间随机生成动物
while True:
    cutTime=time.time()         #定义当前时间
    if (cutTime-startTime)>10:  #定义游戏时常，为调试方便设置为10秒
        break
    else:
        roomNum = randint(0, 9)
        cntanimal=roomLists[roomNum]       #随机调用房间
        while True:                     #一次游戏循环
            str=input(f'现在是{roomNum+1}号房间，请敲门或直接喂肉或草！')
            if str=='敲门':           #若敲门则吼一下，减5斤
                cntanimal.roal()
                cntanimal.static_roal()
                print(cntanimal.name)       #为调试方便打印出当前动物及体重
                print(cntanimal.tweight)
                continue
            elif str=='草' or str=='肉':      #喂食
                cntanimal.food(str)
                print(cntanimal.name)           #为调试方便，打印出当前动物及体重
                print(cntanimal.tweight)
                break
            else:
                print('输入错误，请重新输入')         #输入容错
                continue
lists=[0]*10
for i in range(0,10):
    animal=roomLists[i]
    lists[i]=([animal.name,animal.tweight])
print(lists)                                        #打印出最终房间的动物及体重









