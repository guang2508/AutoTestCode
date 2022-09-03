# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
def keys_and_values(dict):
    klist=[]
    vlist=[]
    alist=['','']
    for i in dict:
        klist.append(i)
        vlist.append(dict[i])
    # print(klist)
    alist[0]=klist
    alist[1]=vlist
    print(alist)
keys_and_values({ "a": "Apple", "b": "Microsoft", "c": "Google" })
