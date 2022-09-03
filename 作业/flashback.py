def  mySort(listSort):
    newList=[]
    for one in range(0,len(listSort)):
        for i in range(len(listSort)-1,one,-1):
            if listSort[i]<listSort[i-1]:
                listSort[i],listSort[i-1]=listSort[i-1],listSort[i]
        newList.append(listSort[one])
    return newList
wr=input('请输入一串数字，用逗号分隔：')
listS=wr.split(',')
for one in range(0,len(listS)-1):
    if listS[one].isdigit()!=True:
        print('您的输入有误')
        exit()
print (mySort(listS))






