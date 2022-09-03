# -*- coding: utf-8 -*-
import random
import time
class Tiger:
    def __init__(self,weight=200):
        self.name="老虎"
        self.weight=weight

    def feed(self,food):
        if food=="meat":
            self.weight += 10
        else:
            self.weight -= 10

    def knock(self):
        print('Wow~~~~~')
        self.weight -= 5

class Sheep:
    def __init__(self,weight=100):
        self.name="羊"
        self.weight=weight

    def feed(self,food):
        if food=="grass":
            self.weight += 10
        else:
            self.weight -= 10

    def knock(self):
        print("mie~~~")
        self.weight -= 5

class RoomList:
    roomList=[]
    for i in range(1,11):
        if random.randint(0,1) == 0:
            animal=Tiger()
            roomList.append(animal)
        else:
            animal=Sheep()
            roomList.append(animal)

print("游戏开始，倒计时20秒")
room=RoomList()
animalList=room.roomList
starttime=time.time()
while True:
    endtime = time.time()
    if endtime-starttime >10 :
        break
    roomNum=random.randint(1,10)
    selectAction=input(f"现在是{roomNum}号房间，请问敲门还是喂食，喂食输入0，敲门输入1")
    if selectAction == "0":
        feed=input("选择喂草还是肉，喂肉输入meat，喂草输入grass")
        animalList[roomNum - 1].feed(feed)

    elif selectAction == "1":
        animalList[roomNum-1].knock()
result=[]
for i in animalList:
    result.append({i.name:i.weight})
print(result)

