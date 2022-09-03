# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-19
def count_num_al(str1):
    str1=list(str1)
    dict1={'字母':0,'数字':0}
    for i in str1:
        if i.isdigit():
            dict1['数字'] +=1
        if i.isalpha():
            dict1['字母'] +=1
    for i in dict1:
        print(f'{i}{dict1[i]}')
str1=input()
count_num_al(str1)