# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-07-08
from robot.api.logger import console
def check_score(score):
    if int(score)>=60:
        console('恭喜你及格了')
    else:
        console('回去继续复习吧')