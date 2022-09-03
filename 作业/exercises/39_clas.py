# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
class printInput():
    def __init__(self):
        self.str1=''
    def getString(self):
        self.str1=input()
        # return str1
    def printString(self):
        # str2=self.getString()
        # print(str2.upper())
        print(self.str1.upper())
if __name__ == '__main__':
    cm=printInput()
    cm.getString()
    cm.printString()