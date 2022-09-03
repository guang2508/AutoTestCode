# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19

def count_type(str1):
    str1=list(str1)
    count_num=0
    count_zimu=0
    count_kongge=0
    count_qita=0
    for i in str1:
        if i.isdigit():
            count_num += 1
        elif i.isalpha():
            count_zimu += 1
        elif i == ' ':
            count_kongge += 1
        else:
            count_qita += 1
    return count_num,count_zimu,count_kongge,count_qita
str1='+0-0skahe817jashf wet1'
count_num,count_zimu,count_kongge,count_qita=count_type(str1)
print(count_num,count_zimu,count_kongge,count_qita)