# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
# def alphabet_index(str1):
#     str1=list(str1)
#     for i in range(0, len(str1)):
#         if str1[i].isalpha() and str1[i].isupper():
#             str1[i]= str(ord(str1[i]) - 64)
#         elif str1[i].isalpha() and str1[i].islower():
#             str1[i] = str(ord(str1[i]) - 96)
#         else:
#             str1[i]= ''
#     for i in str1:
#         if i=='':
#             str1.remove(i)
#
#     str2=(' '.join(str1).strip())
#     return str2
# print(alphabet_index("Wow, does that work?"))

def alphabet_index(str1):
    str1=list(str1)
    alist=[]
    for i in range(0, len(str1)):
        if str1[i].isalpha() and str1[i].isupper():
            str1[i]= str(ord(str1[i]) - 64)
            alist.append(str1[i])
        elif str1[i].isalpha() and str1[i].islower():
            str1[i] = str(ord(str1[i]) - 96)
            alist.append(str1[i])
        else:
            str1[i]= ''
    str2=(' '.join(alist))
    return str2
print(alphabet_index("Wow, does that work?"))