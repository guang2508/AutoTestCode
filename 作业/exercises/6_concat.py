
def connncat(alist,blist):
    if type(alist)==list and type(blist)==list:
        clist=alist+blist
        return clist
    else:
        return '输入的数据有误'
al=[1,3,5]
bl=[2,4,6]
print(connncat(al,bl))