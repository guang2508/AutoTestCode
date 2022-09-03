import random
import datetime
class CreateRoom:
    def __init__(self):
        pass
    def roominfo(self):
        roomList=[]
        for i in range(1,11):
            roomType=random.randint(0,1)
            if roomType==0:
                roomAnimal="tiger"
                roomList.append([roomAnimal,Tiger().weight])
            else:
                roomAnimal="sheep"
                roomList.append([roomAnimal,Sheep().weight])
        return roomList


class Tiger:
    def __init__(self,weight=200):
        self.weight=weight
    def food(self,food):
        if food==1: #1是肉，2是草
            self.weight += 10
        elif food==2:
            self.weight -= 10
    def knock(self):
        print('Wow!!!')
        self.weight -= 5

class Sheep:
    def __init__(self,weight=100):
        self.weight=weight
    def food(self,food):
        if food==2: #1是肉，2是草
            self.weight += 10
        elif food==1:
            self.weight -= 10
    def knock(self):
        print('mie~~~')
        self.weight -= 5


roomlist=CreateRoom().roominfo()
print(roomlist)
startTime=datetime.datetime.now()
print('游戏开始')
while (datetime.datetime.now()-startTime).seconds<10:
    roomnum=random.randint(1,10)
    roominfo=roomlist[roomnum-1]
    if roominfo[0]=='sheep':
        aminal = Sheep(roominfo[1])
    else:
        aminal = Tiger(roominfo[1])
    num=input(f'现在是{roomnum}号房间，请问是敲门还是喂食，喂食输入1，敲门输入2')
    try:
        if num == '1':
            pass
        elif num == '2':
            aminal.knock()
            roominfo[1]=aminal.weight


        foodnum = input('请问喂什么？1是肉，2是草')
        aminal.food(int(foodnum))
        roominfo[1] = aminal.rweight
    except:
        print('输入不正确')
print(roomlist)





