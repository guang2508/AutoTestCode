i=2
avg=1
def func(num):
    if num>2:
        return num * func(num-1)
    else:
        return num
print(func(5))
#
#
#
# print(func(5))

# def jc(n):
#     if n==1:
#         return 1
#     else:
#         return n*jc(n-1)
# print(jc(5))