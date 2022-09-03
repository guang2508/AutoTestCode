# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
def replace(str1,str2):
    list2=str2.split('-')
    string = list(str1)
    for i in range(0,len(str1)):
        if str1[i] >= list2[0] and str1[i] <= list2[1]:

            string[i]='#'
            # str1.replace('str1[i]','#')
    return ''.join(string)
str1=""
str2="i-i"
print(replace(str1,str2))
