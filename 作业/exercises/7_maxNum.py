# import math
# flag=1
# def findLargestNum(p1):
#     a=str(p1)
#     for i in range(0,math.floor(len(a)/2)):
#         if a[i]==a[len(a)-1-i]:
#             pass
#         else:
#             global flag
#             flag=0
#             break
# a=12321
# findLargestNum(a)
# if flag==0:
#     print(False)
# else:
#     print(True)
############-------------------###############

# from collections import Counter
# list=[1,1,1,2,3,4,1,2,5,5,5]
# result=[]
# num_Count=Counter(list)
# # print(num_Count)
# # print(num_Count[0])
# # print(type(num_Count[1]))
# # print(num_Count[2])
# for i in list:
#
#     if (int(num_Count[i])%2==0) and (i not in result):
#         result.append(i)
# print(result)

# def findmax(alist):
#     # if (i for i in alist).isdigit:
#         maxlist=alist[0]
#         for i in range(1,len(alist)):
#             if alist[i]>maxlist:
#                 maxlist=alist[i]
#         return maxlist
# al=[4, 5, 1, 3]
# print(findmax(al))
def findmax(alist):
    return max(alist)
print(findmax([4, 5, 1, 3]))
