def animals(chken_legs,cow_legs,pig_legs):
    legs=chken_legs*2+cow_legs*4+pig_legs*4
    return legs
chken_num=input('鸡的个数：')
cow_num=input('奶牛的个数：')
pig_num=input('猪的个数：')
if chken_num.isdigit() and cow_num.isdigit() and pig_num.isdigit():
    print(animals(int(chken_num),int(cow_num),int(pig_num)))
else:
    print('输入有误')