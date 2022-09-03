# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-27
wrongnum=0
while True:
    name=input()

    passwds=input()

    if name!='yangxiaoer' or passwds!='123456':
        wrongnum+=1
        if wrongnum>3:
            print('错误超过3次，请明天再试')
            break
        print(f'输入错误{wrongnum}次，请重新输入')
        continue
    else:
        print("输入正确")
        break