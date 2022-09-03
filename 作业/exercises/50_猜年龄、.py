# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-27
while True:
    guessAge=input("请输入猜测的年龄：")
    if guessAge.isdigit() :
        if int(guessAge)>48:
            print('大了,再猜')
        elif    int(guessAge)==48:
            print('恭喜你，答对了')
            break
        else:
            print('小了')
    else:
        print('输入错误，请重新输入')

