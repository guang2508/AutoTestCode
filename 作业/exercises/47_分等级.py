# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-22
def grades(score):
    if score>=90:
        return 'A'
    elif 89>=score>=60:
        return 'B'
    elif score<60:
        return 'C'
    else:
        return '输入错误'
score=89
print(grades(score))