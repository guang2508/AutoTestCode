#coding=utf-8
'''
Created on 2017年10月31日

@author: LIli
'''
import os
import sys

def listdir(path,lists):
    for file in os.listdir(path):  
        file_path = os.path.join(path, file)  
        if os.path.isdir(file_path):  
            listdir(file_path,lists)  
        elif 'txt' in os.path.splitext(file_path)[1]:
            #print file_path
            lists[file_path]=get_FileCreateTime(file_path)
            
def get_FileCreateTime(filePath):   
    t = os.path.getctime(filePath)
    return t

def sortfilebyctime(lists):
    orderlist = sorted(lists.items(),key=lambda e:e[1],reverse=False)
    return orderlist
if __name__=='__main__':
    lists={}
    path=r"C:\Users\LIli\Desktop\lis"
    listdir(path,lists)
    orderlists=sortfilebyctime(lists)
    for item in orderlists:
        print (item[0])
