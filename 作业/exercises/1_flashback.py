# def flashback(strs):
#     lists = strs.split(',')
#     i=len(lists)
#     newlist=[]
#     flag=1
#     for i in range(len(lists)-1,-1,-1):
#         if ((lists[i]).strip()).isdigit() or lists[i]=='':
#
#             newlist.append(lists[i])
#         else:
#             print('输入有误！')
#             flag=0
#             break
#     if flag==1:
#         print(newlist)
#
# str=input('请输入一串数字,以逗号间隔：')
# flashback(str)
#
# def resr(alist):
#     alist.reverse()
#     return alist
# alist=[3,'a',4]
# print(resr(alist))
def reversew(num_list):
    if type(num_list) != list:
        print("请输入一个列表")
    else:
        new_list=[]
        for i in range(len(num_list)-1,-1,-1):
            new_list.append(num_list[i])
        return new_list
ll=[9,8,77,7,8]
print(reversew(ll))
print(ll)