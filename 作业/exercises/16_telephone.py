# -*- coding: utf-8 -*-
#   __author__:汤继光
#   2020-05-14
def validate_phone(phoneNum):
    if str(phoneNum).isdigit() and len(str(phoneNum))==11 and str(phoneNum).startswith('1'):
        return True
    else:
        return False

phoneNum='13423445566'
print(validate_phone(phoneNum))