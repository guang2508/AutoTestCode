# -*- coding: utf-8 -*-
#   __author__:Administrator
#   2019-12-02
import subprocess
p=subprocess.Popen(
    'python test5.py',
    stdin=subprocess.PIPE,
stdout=subprocess.PIPE,
stderr=subprocess.PIPE,
    encoding='utf8'
)
inplist=['1','2','3']
out,err=p.communicate('\n'.join(inplist))
print('out=',out)
print('err=',err )
