# def tri_area(end,high):
#     area=end*high/2
#     return area
# end=input('输入三角形的底：')
# high=input('输入三角形的高：')
# if end.isdigit() and high.isdigit():
#     area=tri_area(float(end),float(high))
#     print(area)
# else:
#     print('输入有误！')
def areass(end,high):

    if end.isdigit()==True and high.isdigit()==True:
        return (int(end)*int(high)/2)

end = input('底')
high = input('高')
areass(end,high)
print(areass(end,high))