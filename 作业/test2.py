# -*- coding: utf-8 -*-

class Tiger:
    def __init__(self,weight=200):
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
        self.wight=weight

    def feed(self,food):
        if food=="grass":
            self.wight += 10
        else:
            self.wight -= 10

    def knock(self):
        print("mie~~~")
        self.wight -= 5

class