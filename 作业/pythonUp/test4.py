# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-02
# import os
# os.system('ipconfig')
# print('after')
import subprocess
ret=subprocess.check_output(['pip','list'])
print(ret.decode("utf8"))