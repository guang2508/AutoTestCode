# num= input('请输入一个0--100的数字：')
# while 1:
#     try:
#         num=int(num)
#         if num <0 :
#             num=input('输入不正确，请重新输入一个0--100的数字：')
#         else:
#             break
#     except ValueError:
#         num=input('输入不正确，请重新输入一个0--100的数字：')

import random
randomNum=random.randint(0,100)
for i in range(0,7):
    num = input('请输入一个0--100的数字：')
    while 1:
        try:
            num = int(num)
            if num < 0:
                num = input('输入不正确，请重新输入一个0--100的数字：')
            else:
                break
        except ValueError:
            num = input('输入不正确，请重新输入一个0--100的数字：')
    if num>randomNum:
        print(f'大了,你还剩{6-i}次机会')
    elif num<randomNum:
        print(f'小了,你还剩{6-i}次机会')
    else:
        print('恭喜你答对了')
        break
    i += 1
    if i==7:
        print('游戏结束，你失败了')

