# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
# def findodd(alist):
#     aa=set(alist)
#     resa={}
#     for i in aa:
#         resa[i]=alist.count(i)
#     return resa
# alist=[10,11]
# print(findodd(alist))
# ss=findodd(alist)
# for i in ss:
#     if ss[i]%2 != 0:
#         print(i)
def findoo(alist):
    ret=[]
    for i in alist:
        if alist.count(i)%2 != 0 and i not in ret:

            ret.append(i)
    return ret
alist=[20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]
print(findoo(alist))

