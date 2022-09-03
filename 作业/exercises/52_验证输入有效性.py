# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-27
passwords='ABd1234@1,a F1#,2w3E*,2We3345'
pwdslist=passwords.split(',')
for i in pwdslist:
    if len(i)>=6 and len(i)<=12:
        pwdlist=list(i)
        # print(pwdlist)
        flaga=False
        flagA=False
        flag0=False
        flagt=False
        for j in pwdlist:
            if j.isdigit():
              flag0=True
            elif j.isupper():
                flagA=True
            elif j.islower():
                flaga=True
            elif j in ['$','#','@']:
                flagt=True
        if flaga and flagA and flag0 and flagt:
            print(f'密码: {i} 正确')
        else:
            print(f'密码: {i} 错误')

    else:
        print(f'密码: {i} 错误')