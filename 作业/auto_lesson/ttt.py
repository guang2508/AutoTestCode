list1=[2,8,4,25,42,14,4]
for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j+1]<list1[j]:
            list1[j+1],list1[j]=list1[j],list1[j+1]
print(list1)