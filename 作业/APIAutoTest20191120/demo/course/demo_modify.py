import requests
from config import HOST
payload={
    'action':'modify_course',
    'id':'1545',
    'newdata':'''{
              "name":"初中wwdddd化学",
              "desc":"初中化学dddd课程",
              "display_idx":"4"
            }
            '''
    }
r=requests.put(f'{HOST}/api/mgr/sq_mgr/',data=payload)
print(r.text)

