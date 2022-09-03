# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-21
def bonuses(profit):
    if profit <=10:
        bonus=profit*0.1
    elif 10<profit<=20:
        bonus=10*0.1+(profit-10)*0.075
    elif 20<profit<=40:
        bonus=10*0.1+10*0.075+(profit-20)*0.05
    elif 40<profit<=60:
        bonus=10*0.1+10*0.075+20*0.05+(profit-40)*0.03
    elif 60<profit<=100:
        bonus=10*0.1+10*0.075+20*0.05+20*0.03+(profit-60)*0.015
    elif profit>100:
        bonus = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015+(profit-100)*0.01
    return bonus
profit=30
print(bonuses(profit))