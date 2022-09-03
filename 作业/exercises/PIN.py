# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-01
##判断纯数字
# def pin(PIN):
#     if PIN.isdigit():
#         if len(PIN)==4 or len(PIN)==6:
#             return True
#     return False
# is_valid_PIN=input('请输入PIN：')
# result=pin(is_valid_PIN)
# print(result)

#判断大写
# list=[]
# def upper(num):
#     for i in range(0,len(num)):
#         if num[i].isupper():
#             list.append(i)
#     return list
# indexOfCaps=input("输入一个字符串：")
# print(upper(indexOfCaps))

# #列表去重
# l1 = ['b','c','d','b','c','a','a']
# l2 = list(set(l1))
# print(l2)
# l2.sort(key=l1.index)
# print(l2)

# #列表数据相加
# def sumer(list):
#     list2=[]
#     sum=0
#     for i in range(0,len(list)):
#         for j in range(0,i+1):
#             sum+=list[j]
#         list2.append(sum)
#         sum = 0
#     return list2
# list1=[1,2,3,4]
# print(sumer(list1))
##法二：
# def accumulate(list):
#     ret = []
#     for one in list:
#         ret.append(sum(list[:one]))
#     return ret
# print(accumulate([1, 2, 3, 4]))

# ###list=[1,2,3]
# ###print(sum(list))


