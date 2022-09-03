# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
# def is_symmetry(aa):
#     if aa.isdigit()==True:
#         for i in range(0,int(len(aa)/2)):
#             if aa[i] != aa[len(aa)-1-i]:
#                 return False
#         return True
#     return '数据有误'
# print(is_symmetry('7'))




def sss(aaa):
    if aaa[::-1]==aaa:
        return True
print(sss('12321'))

