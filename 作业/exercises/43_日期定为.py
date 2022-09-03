# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-21
import datetime
def dayOfYear(day1):
    day1=datetime.datetime.strptime(day1,'%Y-%m-%d')
    str1=f'{day1.year}-01-01'
    day2=datetime.datetime.strptime(str1,'%Y-%m-%d')
    print((day1-day2).days)
day1=input()
dayOfYear(day1)