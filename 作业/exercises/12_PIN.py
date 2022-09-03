# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-11
def is_PIN(str):
    if  len(str)==4 or len(str)==6 and str.isdigit():
        return True
    else:
        return False
str=''
print(is_PIN(str))